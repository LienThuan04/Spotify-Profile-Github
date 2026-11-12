# Spotify-Profile-Github — Spotify "Now Playing" card

- Repo: `github.com/LienThuan04/Spotify-Profile-Github` (branch **`master`**), duy trì bởi `LianHarman(LienThuan04)`. Giấy phép gốc: `THIRD_PARTY_NOTICES.md`.
- Deploy: Vercel → `https://spotify-github-profile-lian-harman.vercel.app/api/view?uid=<spotify_uid>`.
- Stack: Python ≥3.12 (CI chạy 3.11 + 3.12), Flask 3, Firebase Firestore, Pillow + colorgram, Jinja2 templates, pytest.

## Endpoints (`api/app.py` gom tất cả cho Vercel / chạy local)

| Route | Handler | Việc |
|---|---|---|
| `/` | redirect | → `/api/login` |
| `/api/login` | `api/login.py` | redirect sang Spotify OAuth (scope `user-read-currently-playing,user-read-recently-played`) |
| `/api/callback` | `api/callback.py` | đổi `code` → token, lưu `users/<spotify_uid>` vào Firestore, render `callback.html.j2` |
| `/api/view`, `/api/view.svg` | `api/view.py:catch_all` | render card SVG |

## Trang tạo mã nhúng

`api/templates/callback.html.j2` là **Card Studio** sau khi kết nối Spotify. Partial `api/templates/_builder/styles.css` và `builder.js` được Jinja include inline, không cần CDN hay route static. JS thuần: `buildEmbed(config, state)` sinh URL/Markdown/HTML; `getThemeFeatures(theme)` xác định tùy chọn hợp lệ; `mount(document, config)` nối form, preview (debounce 300ms), tab/copy/reset. Cấu hình `uid`/`BASE_URL` truyền bằng `tojson`.

Mặc định: `spotify-card`, eq `bars`, xanh `1ed760`, nền `121212`, bo 10px, ảnh bìa và mở bài khi click bật. `mode` chỉ cho Apple/Spotify Embed; background/equalizer chỉ hiện khi theme hỗ trợ. Tắt ảnh bìa sẽ vô hiệu lấy màu từ bìa. Kiểm JS bằng `node --test tests/test_builder.js` (Node.js 22+); pytest render template trong `tests/test_builder_template.py` không import OAuth/Firebase.

## Luồng `/api/view`

```
catch_all(uid, query params)
  └─ get_song_info(uid)
       └─ get_access_token(uid): cache RAM CACHE_TOKEN_INFO → Firestore → refresh nếu hết hạn
            (refresh trả invalid_grant → xoá user khỏi Firestore → InvalidTokenError)
       ├─ spotify.get_now_playing()       đang phát → is_now_playing
       └─ spotify.get_recently_play()     không phát → chọn ngẫu nhiên 1 bài gần đây
  ├─ load_image() bìa album → base64 (+ colorgram nếu bar_color_cover=true)
  ├─ profanity_check() / remove_remaster() (tuỳ chọn)
  └─ make_svg() → render_template("spotify.<theme>.html.j2")
→ image/svg+xml, Cache-Control: public, max-age=0, s-maxage=10, stale-while-revalidate=3600
```

## Themes

`api/templates/spotify.<theme>.html.j2`: `default`, `compact`, `natemoo-re`, `novatorem`, `karaoke`, `apple`, `spotify-embed`, `spotify-card`, `spotify-bar`, `spotify-album`. Ba theme mới dùng macro CSS/SVG trong `spotify._shared.html.j2`, hỗ trợ `eq_style` (`bars`, `spectrum`, `mirror`, `wave`, `pulse`, `iso`, `ribbon`, `floor`, `none`). Chiều cao + số thanh equalizer của mỗi theme nằm trong `make_svg()` (`api/view.py`). Thiết kế đã duyệt: `docs/DESIGN-spotify.md`. Thêm theme mới: `docs/skills/spotify-card/SKILL.md`.

## Query params

Bảng Options trong `README.md` của repo có đầy đủ 13 tùy chọn của `catch_all()` (gồm `profanity`, `hide_remaster`, `redirect`); `uid` lấy từ trang tạo link sau khi kết nối Spotify. README có preview live cho 10 theme, 9 kiểu sóng và 12 tùy chọn có ảnh; `redirect=true` dùng làm URL liên kết vì trả 302 sang bài hát.

## Env (`.env` ở gốc repo, mẫu: `.env.example`)

| Biến | Ghi chú |
|---|---|
| `SPOTIFY_CLIENT_ID`, `SPOTIFY_SECRET_ID` | Spotify app. |
| `BASE_URL` | vd `http://localhost:3000/api`; `REDIRECT_URI = BASE_URL + "/callback"` phải khớp cấu hình Spotify app. |
| `FIREBASE` | JSON service account, mã hoá **base64**. |
| `TESTING=true` | `util/firestore.py` trả `MagicMock` thay vì Firestore thật. |

## Lệnh

```sh
pip install -r api/requirements.txt
python api/app.py                 # http://localhost:3000/api/login
TESTING=true PYTHONPATH=. pytest tests/ -v     # CI: pytest tests/ --maxfail=5
docker compose up                 # 3 service gunicorn: view:5003, login:5001, callback:5002
```

## Bố cục

- `api/` — handler Flask + `templates/`.
- `util/` — `spotify.py` (gọi Spotify API), `firestore.py`, `profanity.py`, `remaster.py`.
- `api/util` và `api/view.svg.py` là **symlink** git (trỏ `../util/` và `view.py`); trên Windows chúng thành file text — xem `docs/memory/gotchas.md`.
- `img/*.svg` — ảnh minh hoạ theme cho README.
