"""Sinh SVG mẫu cho README và thư mục duyệt, không gọi Spotify/Firestore.

Chạy từ gốc repo:
    .venv/Scripts/python.exe scripts/generate_spotify_examples.py
    .venv/Scripts/python.exe scripts/generate_spotify_examples.py --review-dir <thư mục>
"""

import argparse
import io
import os
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ["TESTING"] = "true"

from PIL import Image
from api.view import EQ_STYLES, SPOTIFY_THEMES, app, make_svg, to_img_b64


def gradient_cover(size=208):
    """Gradient hồng/tím như ảnh bìa trong mockup đã duyệt."""
    image = Image.new("RGB", (size, size))
    stops = [(255, 47, 160), (138, 43, 226), (43, 16, 85)]
    pixels = image.load()
    for y in range(size):
        for x in range(size):
            position = (x + y) / (2 * (size - 1))
            if position < .55:
                start, end, fraction = stops[0], stops[1], position / .55
            else:
                start, end, fraction = stops[1], stops[2], (position - .55) / .45
            pixels[x, y] = tuple(round(a + (b - a) * fraction) for a, b in zip(start, end))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return to_img_b64(buffer.getvalue())


def render_example(theme, cover, state="playing", eq_style="bars", cover_image=True):
    offline = state == "offline"
    return make_svg(
        artist_name="Offline" if offline else "Lazer Boomerang",
        song_name="Currently not playing on Spotify" if offline else "Time To Pretend",
        img="" if offline else cover,
        is_now_playing=state == "playing",
        cover_image=cover_image and not offline,
        theme=theme,
        bar_color="1ed760",
        show_offline=offline,
        background_color="121212",
        mode="light",
        border_radius="8",
        progress_ms=196000 if state == "playing" else 0,
        duration_ms=None if offline else 314000,
        eq_style=eq_style,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-dir", type=Path, help="Thư mục SVG dành cho duyệt bằng mắt")
    args = parser.parse_args()
    random.seed(42)
    cover = gradient_cover()
    image_dir = ROOT / "img"
    image_dir.mkdir(exist_ok=True)
    with app.app_context():
        for theme in SPOTIFY_THEMES:
            (image_dir / f"{theme}.svg").write_text(render_example(theme, cover), encoding="utf-8")
        print(f"Đã sinh 3 ảnh README tại {image_dir}")
        if args.review_dir:
            args.review_dir.mkdir(parents=True, exist_ok=True)
            for theme in SPOTIFY_THEMES:
                for state in ["playing", "recent", "offline"]:
                    path = args.review_dir / f"{theme}-{state}.svg"
                    path.write_text(render_example(theme, cover, state=state), encoding="utf-8")
                path = args.review_dir / f"{theme}-no-cover.svg"
                path.write_text(render_example(theme, cover, cover_image=False), encoding="utf-8")
            for eq_style in EQ_STYLES:
                path = args.review_dir / f"spotify-card-eq-{eq_style}.svg"
                path.write_text(render_example("spotify-card", cover, eq_style=eq_style), encoding="utf-8")
            print(f"Đã sinh 18 SVG duyệt tại {args.review_dir.resolve()}")


if __name__ == "__main__":
    main()
