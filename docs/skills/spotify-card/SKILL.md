---
name: spotify-card
description: Change the Spotify now-playing card in Spotify-SPARK (Spotify Presence Activity Render Kit) — add or edit a theme template, add a query parameter, fix token/Firestore issues, or run it locally. Use whenever the task touches spotify-github-profile/.
---

# Spotify card (Spotify-SPARK)

Bối cảnh repo và luồng request: `docs/PROJECT.md`. Branch mặc định là **`master`**.

## Chuẩn bị chạy local (Windows)

```powershell
# Chạy tại gốc repo
pip install -r api/requirements.txt
$env:PYTHONPATH = '.'          # bắt buộc trên Windows: api/util là symlink bị hỏng
$env:TESTING = 'true'          # Firestore → MagicMock
pytest tests/ -v
```

Chạy server thật cần `.env` (copy `.env.example`; `FIREBASE` là JSON service account dạng base64) rồi `python api/app.py` → `http://localhost:3000/api/login`.

## Thêm theme mới

1. Tạo `api/templates/spotify.<theme>.html.j2` — copy theme gần nhất. Biến template có sẵn: `height`, `num_bar`, `content_bar`, `css_bar`, `title_text`, `artist_name`, `song_name`, `img` (base64), `cover_image`, `bar_color`, `background_color`, `mode`, `is_now_playing`, `progress_data`, `border_radius`.
2. Thêm nhánh `elif theme == "<theme>":` trong `make_svg()` (`api/view.py`) để đặt `height` và `num_bar` (0 nếu không có thanh equalizer). Thiếu nhánh → rơi vào chiều cao của `default`.
3. Nếu theme cần `progress_data` → thêm tên theme vào list `["apple", "spotify-embed"]` trong `make_svg()`.
4. Thêm option vào select theme trong `api/templates/callback.html.j2` (trang sinh URL sau khi login).
5. Thêm ảnh minh hoạ `img/<theme>.svg` và dòng vào bảng `theme` trong `README.md` của repo.
6. Test: thêm case vào `tests/test_api_view.py` gọi `make_svg(..., theme="<theme>", ...)` và assert chiều cao/chuỗi đặc trưng.

Xong khi: `pytest tests/` xanh và `GET /api/view?uid=<uid>&theme=<theme>` trả SVG render đúng trong trình duyệt.

## Thêm query param

Đọc trong `catch_all()` (`api/view.py`) bằng `request.args.get(..., default=...)`; validate input người dùng trước khi đưa vào template (xem cách `border_radius` được kiểm `^\d+$`). Truyền vào `make_svg()` → `rendered_data`. Cập nhật bảng Customization trong `README.md`.

## Lỗi "Invalid Spotify access_token or refresh_token"

Refresh token bị thu hồi → `get_access_token()` đã xoá document `users/<uid>` khỏi Firestore. Cách sửa: đăng nhập lại qua `/api/login` để tạo token mới; `uid` giữ nguyên.

## Đổi header cache

Header nằm ở 2 chỗ trong `catch_all()` (nhánh offline và nhánh chính) và được assert trong `tests/test_api_view.py` + `tests/test_api_view_sg.py` — sửa cả 4 chỗ.
