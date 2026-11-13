"""Card Studio's "Coming soon" tile and footer link send ideas to FEEDBACK_URL or the owner's GitHub profile."""
from pathlib import Path

from flask import Flask, render_template

from util.feedback import OWNER_PROFILE_URL, feedback_url


def render(**context):
    templates = Path(__file__).resolve().parents[1] / "api" / "templates"
    app = Flask(__name__, template_folder=str(templates))
    with app.app_context():
        return render_template("callback.html.j2", uid="demo-user", BASE_URL="https://example.test/api", **context)


def test_feedback_url_accepts_http_urls_and_falls_back_to_github(monkeypatch):
    assert feedback_url("https://lianharman.netlify.app") == "https://lianharman.netlify.app"
    assert feedback_url("  http://example.com/ideas  ") == "http://example.com/ideas"
    for bad in ("", "   ", "javascript:alert(1)", "not a url", "https://"):
        assert feedback_url(bad) == OWNER_PROFILE_URL
    monkeypatch.setenv("FEEDBACK_URL", "https://lianharman.netlify.app")
    assert feedback_url() == "https://lianharman.netlify.app"
    monkeypatch.delenv("FEEDBACK_URL")
    assert feedback_url() == OWNER_PROFILE_URL == "https://github.com/LienThuan04"


def test_builder_shows_a_coming_soon_tile_and_footer_feedback_link():
    html = render(feedback_url="https://lianharman.netlify.app")
    assert "Coming soon" in html
    assert 'class="theme-option theme-soon"' in html
    assert "Suggest a theme or feature" in html
    assert html.count('href="https://lianharman.netlify.app"') == 2
    # The tile is a link, not another theme radio.
    assert 'value="coming-soon"' not in html


def test_builder_falls_back_to_the_github_profile_without_a_feedback_url():
    html = render()
    assert html.count('href="https://github.com/LienThuan04"') >= 2


def test_builder_uses_the_original_app_icon_as_favicon_and_brand_mark():
    from urllib.parse import unquote
    html = render()
    assert '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,' in html
    assert '<img class="brand-mark" src="data:image/svg+xml,' in html
    icon = unquote(html.split('<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,', 1)[1].split('"', 1)[0])
    assert icon.startswith("<svg") and icon.rstrip().endswith("</svg>")
    # The old brand mark reproduced the platform's three-arc logo; the new icon is original artwork.
    assert "M5.3 8.8c4.4-1.3" not in html
    assert "<image" not in icon and "href=" not in icon.replace('url(#', '')
