const assert = require('node:assert/strict');
const { test } = require('node:test');
const { buildEmbed, getThemeFeatures, DEFAULT_STATE, mount } = require('../api/templates/_builder/builder.js');

const config = { uid: 'user +/?&"<>', baseUrl: 'https://example.test/api/' };
const build = (overrides = {}) => buildEmbed(config, { ...DEFAULT_STATE, ...overrides });
const query = (result) => new URL(result.imageUrl).searchParams;

test('default export is a Spotify card whose click target redirects without redirecting the image', () => {
  const result = build();
  assert.equal(query(result).get('theme'), 'spotify-card');
  assert.equal(query(result).get('uid'), 'user +/?&"<>');
  assert.equal(query(result).get('redirect'), null);
  assert.equal(new URL(result.linkUrl).searchParams.get('redirect'), 'true');
  assert.ok(result.markdown.includes(`](${result.linkUrl})`));
  assert.ok(result.html.includes('&amp;theme='));
  assert.ok(!result.html.includes('src="https://example.test/api/view?uid=user +'));
});

test('all nine equalizer choices survive export on each of the three Spotify themes', () => {
  for (const theme of ['spotify-card', 'spotify-bar', 'spotify-album']) {
    for (const eq_style of ['bars', 'spectrum', 'mirror', 'wave', 'pulse', 'iso', 'ribbon', 'floor', 'none']) {
      const params = query(build({ theme, eq_style }));
      assert.equal(params.get('eq_style'), eq_style);
      assert.equal(params.get('bar_color'), '1ed760');
    }
  }
});

test('legacy themes omit unsupported options and use their own equalizer color default', () => {
  const params = query(build({ theme: 'default', eq_style: 'floor', mode: 'dark' }));
  assert.equal(params.get('eq_style'), null);
  assert.equal(params.get('mode'), null);
  assert.equal(params.get('bar_color'), '53b14f');
  for (const theme of ['compact', 'karaoke', 'apple', 'spotify-embed']) {
    const result = query(build({ theme, bar_color: 'ff00aa', bar_color_cover: true }));
    assert.equal(result.get('bar_color'), null);
    assert.equal(result.get('bar_color_cover'), null);
  }
});

test('theme capabilities include both Apple and Spotify Embed color modes', () => {
  for (const theme of ['apple', 'spotify-embed']) {
    assert.equal(getThemeFeatures(theme).mode, true);
    const params = query(build({ theme, mode: 'dark' }));
    assert.equal(params.get('mode'), 'dark');
    assert.equal(params.get('background_color'), null);
  }
  assert.equal(getThemeFeatures('spotify-card').equalizer, true);
  assert.equal(getThemeFeatures('default').equalizer, false);
});

test('customization values appear in both the image URL and generated Markdown', () => {
  const result = build({ bar_color: '#AABBCC', background_color: '#223344', border_radius: 24, cover_image: false, show_offline: true, interchange: true, profanity: true, hide_remaster: true });
  const params = query(result);
  for (const [key, value] of Object.entries({ bar_color: 'aabbcc', background_color: '223344', border_radius: '24', cover_image: 'false', show_offline: 'true', interchange: 'true', profanity: 'true', hide_remaster: 'true' })) {
    assert.equal(params.get(key), value);
  }
  assert.ok(result.markdown.includes(result.imageUrl));
});

test('automatic color is omitted without cover artwork and enabled when artwork returns', () => {
  assert.equal(query(build({ cover_image: false, bar_color_cover: true })).get('bar_color_cover'), 'false');
  assert.equal(query(build({ cover_image: true, bar_color_cover: true })).get('bar_color_cover'), 'true');
});

test('invalid enums/colors/radius normalize to working supported values', () => {
  const params = query(build({ theme: 'missing', eq_style: 'missing', bar_color: 'invalid', background_color: 'invalid', border_radius: 'oops' }));
  assert.equal(params.get('theme'), 'spotify-card');
  assert.equal(params.get('eq_style'), 'bars');
  assert.equal(params.get('bar_color'), '1ed760');
  assert.equal(params.get('background_color'), '121212');
  assert.equal(params.get('border_radius'), '10');
  assert.equal(query(build({ border_radius: -3 })).get('border_radius'), '0');
});

test('disabling song links keeps the project as the link destination', () => {
  assert.equal(build({ open_song: false }).linkUrl, 'https://github.com/LienThuan04/Spotify-Profile-Github');
});

function pageFixture() {
  const ids = ['builder-form', 'example-view', 'embed-code', 'code-hint', 'code-label', 'code-panel', 'copy-status', 'preview-message', 'preview-error', 'equalizer-field', 'mode-field', 'background-field', 'bar-color-field', 'auto-color-field', 'auto-color', 'auto-color-hint', 'bar-color', 'bar-color-value', 'background-value', 'radius-value', 'preview-theme', 'open-preview', 'refresh-preview', 'reset-button', 'background-color', 'copy-button'];
  const elements = new Map();
  function element(id, dataset = {}) {
    const listeners = {};
    return { id, dataset, value: '', textContent: '', hidden: false, disabled: false, attributes: {},
      addEventListener(type, callback) { (listeners[type] ||= []).push(callback); },
      emit(type, detail = {}) { return Promise.all((listeners[type] || []).map(callback => callback({ target: this, preventDefault() {}, ...detail }))); },
      setAttribute(key, value) { this.attributes[key] = value; },
      removeAttribute(key) { delete this[key]; },
      click() { return this.emit('click'); }, focus() {}, select() {},
    };
  }
  for (const id of ids) elements.set(id, element(id));
  const tabs = ['markdown', 'html', 'url'].map(format => element('tab-' + format, { tab: format }));
  const form = elements.get('builder-form');
  let selectedTheme = 'spotify-card';
  form.querySelector = () => ({ closest: () => ({ querySelector: () => ({ textContent: selectedTheme }) }) });
  form.reset = () => { selectedTheme = 'spotify-card'; };
  const copied = [];
  const doc = { getElementById: id => elements.get(id), querySelectorAll: () => tabs, defaultView: { navigator: { clipboard: { writeText: async value => { copied.push(value); } } } }, execCommand: () => false };
  mount(doc, config);
  return { doc, tabs, copied, get: id => elements.get(id),
    async change(name, value, type = 'select-one') {
      if (name === 'theme') selectedTheme = value;
      await form.emit('input', { target: { name, value, type, checked: Boolean(value) } });
    }
  };
}

test('controls update export immediately, preserve colors across themes, and debounce the preview', async t => {
  t.mock.timers.enable({ apis: ['setTimeout'] });
  const page = pageFixture();
  await page.change('bar_color', '#ff00aa', 'color');
  await page.change('eq_style', 'ribbon');
  await page.change('theme', 'apple', 'radio');
  assert.equal(page.get('equalizer-field').hidden, true);
  assert.equal(page.get('mode-field').hidden, false);
  assert.ok(!page.get('embed-code').value.includes('eq_style='));
  await page.change('theme', 'spotify-bar', 'radio');
  assert.ok(page.get('embed-code').value.includes('eq_style=ribbon'));
  assert.ok(page.get('embed-code').value.includes('bar_color=ff00aa'));
  t.mock.timers.tick(301);
  assert.equal(new URL(page.get('example-view').src).searchParams.get('theme'), 'spotify-bar');
  await page.get('reset-button').click();
  assert.equal(new URL(page.get('example-view').src).searchParams.get('theme'), 'spotify-card');
  assert.equal(new URL(page.get('example-view').src).searchParams.get('bar_color'), '1ed760');
});

test('preview error after a successful load exposes a readable retry message', async t => {
  t.mock.timers.enable({ apis: ['setTimeout'] });
  const page = pageFixture();
  await page.get('example-view').emit('load');
  assert.equal(page.get('preview-message').hidden, true);
  await page.get('example-view').emit('error');
  assert.equal(page.get('preview-message').hidden, false);
  assert.equal(page.get('preview-error').hidden, false);
  await page.get('refresh-preview').click();
  await page.get('example-view').emit('load');
  assert.equal(page.get('preview-error').hidden, true);
  assert.equal(page.get('example-view').hidden, false);
});

test('tabs copy the selected format and denied clipboard access does not report success', async t => {
  t.mock.timers.enable({ apis: ['setTimeout'] });
  const page = pageFixture();
  await page.tabs[1].click();
  assert.ok(page.get('embed-code').value.startsWith('<a href='));
  assert.equal(page.get('code-panel').attributes['aria-labelledby'], 'tab-html');
  await page.get('copy-button').click();
  assert.ok(page.copied[0].startsWith('<a href='));
  assert.equal(page.get('copy-status').textContent, 'Copied to clipboard.');
  await page.tabs[2].click();
  assert.ok(page.get('embed-code').value.startsWith('https://example.test/api/view?'));
  page.doc.defaultView.navigator.clipboard.writeText = async () => { throw new Error('Denied'); };
  await page.get('copy-button').click();
  assert.equal(page.get('copy-status').textContent, 'Select the code and copy it manually.');
});
