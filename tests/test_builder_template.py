"""Render the actual builder without OAuth or Firebase credentials."""
from html.parser import HTMLParser
import json
from pathlib import Path

from flask import Flask, render_template


class BuilderPage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.label_targets = []
        self.config = ""
        self.in_config = False
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "label" and "for" in attrs:
            self.label_targets.append(attrs["for"])
        if tag == "script":
            self.in_config = attrs.get("id") == "builder-config"
            self.scripts.append(attrs)

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_config = False

    def handle_data(self, data):
        if self.in_config:
            self.config += data


def render_builder(uid="demo-user", base_url="https://example.test/api"):
    templates = Path(__file__).resolve().parents[1] / "api" / "templates"
    app = Flask(__name__, template_folder=str(templates))
    with app.app_context():
        return render_template("callback.html.j2", uid=uid, BASE_URL=base_url)


def test_builder_config_preserves_uid_without_breaking_out_of_json_script():
    uid = '</script><script>alert("test")</script>&é'
    html = render_builder(uid)
    page = BuilderPage()
    page.feed(html)
    assert json.loads(page.config) == {"uid": uid, "baseUrl": "https://example.test/api"}
    assert len(page.scripts) == 2
    assert all("src" not in script for script in page.scripts)


def test_builder_controls_have_unique_ids_and_reachable_labels():
    page = BuilderPage()
    page.feed(render_builder())
    assert len(page.ids) == len(set(page.ids))
    assert set(page.label_targets) <= set(page.ids)
    assert {"builder-form", "example-view", "embed-code", "border-radius", "copy-button", "reset-button"} <= set(page.ids)
