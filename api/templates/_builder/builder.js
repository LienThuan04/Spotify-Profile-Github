(function () {
  'use strict';
  const PROJECT_URL = 'https://github.com/LienThuan04/Spotify-SPARK';
  const THEMES = ['spotify-card', 'spotify-bar', 'spotify-album', 'spotify-mini', 'spotify-vinyl', 'spotify-banner', 'spotify-glass', 'spotify-mobile', 'default', 'compact', 'natemoo-re', 'novatorem', 'karaoke', 'apple', 'spotify-embed'];
  const EQ_STYLES = ['bars', 'spectrum', 'mirror', 'wave', 'pulse', 'iso', 'ribbon', 'floor', 'dots', 'vu', 'ring', 'ripple', 'heartbeat', 'pixel', 'glow', 'bubbles', 'skyline', 'tunnel', 'none'];
  const DEFAULT_STATE = Object.freeze({ theme: 'spotify-card', eq_style: 'bars', bar_color: null, background_color: '121212', border_radius: 10, mode: 'dark', cover_image: true, open_song: true, show_offline: false, interchange: false, hide_remaster: false, profanity: false, bar_color_cover: false });

  function getThemeFeatures(theme) {
    const equalizer = ['spotify-card', 'spotify-bar', 'spotify-album', 'spotify-mini', 'spotify-vinyl', 'spotify-banner', 'spotify-glass', 'spotify-mobile'].includes(theme);
    return {
      equalizer,
      barColor: equalizer || ['default', 'natemoo-re', 'novatorem'].includes(theme),
      background: equalizer || ['default', 'compact', 'karaoke'].includes(theme),
      mode: ['apple', 'spotify-embed'].includes(theme),
      defaultBarColor: equalizer ? '1ed760' : '53b14f'
    };
  }

  function normalizeColor(value, fallback) {
    const color = String(value || '').replace(/^#/, '');
    return /^[0-9a-f]{6}$/i.test(color) ? color.toLowerCase() : fallback;
  }

  function buildEmbed(config, state) {
    const theme = THEMES.includes(state.theme) ? state.theme : DEFAULT_STATE.theme;
    const features = getThemeFeatures(theme);
    const viewUrl = new URL(String(config.baseUrl).replace(/\/+$/, '') + '/view');
    const params = viewUrl.searchParams;
    params.set('uid', config.uid);
    params.set('theme', theme);
    for (const key of ['cover_image', 'show_offline', 'interchange', 'profanity', 'hide_remaster']) params.set(key, String(Boolean(state[key])));
    const radius = Number(state.border_radius);
    params.set('border_radius', String(Number.isFinite(radius) ? Math.max(0, Math.min(50, Math.round(radius))) : 10));
    if (features.equalizer) params.set('eq_style', EQ_STYLES.includes(state.eq_style) ? state.eq_style : 'bars');
    if (features.background) params.set('background_color', normalizeColor(state.background_color, '121212'));
    if (features.barColor) {
      params.set('bar_color', normalizeColor(state.bar_color, features.defaultBarColor));
      params.set('bar_color_cover', String(Boolean(state.bar_color_cover && state.cover_image)));
    }
    if (features.mode) params.set('mode', state.mode === 'light' ? 'light' : 'dark');
    const imageUrl = viewUrl.href;
    let linkUrl = PROJECT_URL;
    if (state.open_song) {
      const redirectUrl = new URL(viewUrl.href);
      redirectUrl.search = new URLSearchParams({ uid: config.uid, redirect: 'true' }).toString();
      linkUrl = redirectUrl.href;
    }
    const escapeAttribute = (value) => value.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
    return {
      imageUrl, linkUrl,
      markdown: `[![Spotify-SPARK](${imageUrl})](${linkUrl})`,
      html: `<a href="${escapeAttribute(linkUrl)}">\n  <img src="${escapeAttribute(imageUrl)}" alt="Spotify now playing" />\n</a>`
    };
  }

  function mount(doc, config) {
    let state = { ...DEFAULT_STATE };
    let format = 'markdown';
    let previewTimer;
    let copyTimer;
    let embed;
    const $ = (id) => doc.getElementById(id);
    const form = $('builder-form');
    const image = $('example-view');
    const code = $('embed-code');
    const tabs = Array.from(doc.querySelectorAll('[data-tab]'));
    const hint = { markdown: 'Paste this into your GitHub profile README.md.', html: 'Use this HTML in your README or on your website.', url: 'Use this URL wherever an image source is accepted.' };
    const labels = { markdown: 'Markdown embed code', html: 'HTML embed code', url: 'Card image URL' };

    function renderCode() {
      code.value = format === 'url' ? embed.imageUrl : embed[format];
      $('code-hint').textContent = hint[format];
      $('code-label').textContent = labels[format];
      $('code-panel').setAttribute('aria-labelledby', 'tab-' + format);
      $('copy-status').textContent = '';
      for (const tab of tabs) {
        const active = tab.dataset.tab === format;
        tab.setAttribute('aria-selected', String(active));
        tab.tabIndex = active ? 0 : -1;
      }
    }

    function refreshPreview() {
      clearTimeout(previewTimer);
      image.dataset.loading = 'true';
      $('preview-message').textContent = 'Updating your preview…';
      $('preview-message').hidden = false;
      $('preview-error').hidden = true;
      // A fresh image request also retries after a temporary card error.
      image.removeAttribute('src');
      image.src = embed.imageUrl;
    }

    function render(immediate = false) {
      const features = getThemeFeatures(state.theme);
      $('equalizer-field').hidden = !features.equalizer;
      $('mode-field').hidden = !features.mode;
      $('background-field').hidden = !features.background;
      $('bar-color-field').hidden = !features.barColor;
      $('auto-color-field').hidden = !features.barColor;
      $('auto-color').disabled = !state.cover_image;
      $('auto-color-hint').textContent = state.cover_image ? 'Let the cover choose the equalizer color.' : 'Turn on album artwork to use this option.';
      $('bar-color').disabled = state.bar_color_cover && state.cover_image;
      const barColor = normalizeColor(state.bar_color, features.defaultBarColor);
      $('bar-color').value = '#' + barColor;
      $('bar-color-value').textContent = '#' + barColor.toUpperCase();
      $('background-value').textContent = '#' + state.background_color.toUpperCase();
      $('radius-value').textContent = state.border_radius + ' px';
      const selected = form.querySelector('input[name="theme"]:checked');
      $('preview-theme').textContent = selected.closest('label').querySelector('strong').textContent;
      embed = buildEmbed(config, state);
      $('open-preview').href = embed.imageUrl;
      renderCode();
      clearTimeout(previewTimer);
      if (immediate) refreshPreview();
      else previewTimer = setTimeout(refreshPreview, 300);
    }

    function handleInput(event) {
      const input = event.target;
      if (!input.name || (input.type === 'radio' && !input.checked)) return;
      if (input.type === 'checkbox') state[input.name] = input.checked;
      else if (input.name === 'bar_color' || input.name === 'background_color') state[input.name] = input.value.slice(1);
      else if (input.name === 'border_radius') state.border_radius = Number(input.value);
      else state[input.name] = input.value;
      render();
    }
    form.addEventListener('input', handleInput);
    form.addEventListener('submit', (event) => event.preventDefault());
    $('refresh-preview').addEventListener('click', refreshPreview);
    $('reset-button').addEventListener('click', () => {
      form.reset();
      state = { ...DEFAULT_STATE };
      $('background-color').value = '#121212';
      render(true);
    });
    image.addEventListener('load', () => {
      image.dataset.loading = 'false';
      image.hidden = false;
      $('preview-message').hidden = true;
      $('preview-error').hidden = true;
    });
    image.addEventListener('error', () => {
      image.dataset.loading = 'false';
      image.hidden = true;
      $('preview-message').textContent = 'Your preview is taking a break.';
      $('preview-message').hidden = false;
      $('preview-error').hidden = false;
    });
    for (const [index, tab] of tabs.entries()) {
      tab.addEventListener('click', () => { format = tab.dataset.tab; renderCode(); });
      tab.addEventListener('keydown', (event) => {
        let next;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        else if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
        else if (event.key === 'Home') next = 0;
        else if (event.key === 'End') next = tabs.length - 1;
        if (next === undefined) return;
        event.preventDefault();
        tabs[next].focus();
        tabs[next].click();
      });
    }
    $('copy-button').addEventListener('click', async () => {
      const value = code.value;
      const clipboard = doc.defaultView.navigator.clipboard;
      let copied = false;
      try {
        if (clipboard && clipboard.writeText) { await clipboard.writeText(value); copied = true; }
      } catch (_) { /* Fall back to the selected code on restricted browsers. */ }
      if (!copied) {
        code.focus();
        code.select();
        try { copied = Boolean(doc.execCommand && doc.execCommand('copy')); } catch (_) { copied = false; }
      }
      $('copy-status').textContent = copied ? 'Copied to clipboard.' : 'Select the code and copy it manually.';
      clearTimeout(copyTimer);
      copyTimer = setTimeout(() => { $('copy-status').textContent = ''; }, 4000);
    });
    render(true);
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { buildEmbed, getThemeFeatures, DEFAULT_STATE, mount };
  else mount(document, JSON.parse(document.getElementById('builder-config').textContent));
})();
