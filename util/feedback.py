"""Where Card Studio sends visitors with theme and feature ideas."""
import os
from urllib.parse import urlsplit

OWNER_PROFILE_URL = "https://github.com/LienThuan04"


def feedback_url(value=None):
    """Return FEEDBACK_URL (or `value`) when it is an http(s) URL, else the owner's GitHub profile."""
    raw = (os.getenv("FEEDBACK_URL", "") if value is None else value).strip()
    parts = urlsplit(raw)
    return raw if parts.scheme in ("http", "https") and parts.netloc else OWNER_PROFILE_URL
