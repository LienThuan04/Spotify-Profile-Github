# Gotchas — Spotify-Profile-Github

Triệu chứng → nguyên nhân → cách xử lý. Ghi thêm sau khi xác minh; bỏ mục đã hết hiệu lực.

## Card trên GitHub

- **Card Spotify/Discord hiện ảnh vỡ trên trang profile** → GitHub tải ảnh qua proxy `camo.githubusercontent.com`, bỏ cuộc nếu server phản hồi chậm (cold start Vercel 4s+) → đặt header `Cache-Control: public, ..., s-maxage=..., stale-while-revalidate=3600` để Vercel edge trả bản cache. Đã áp dụng cho cả 2 repo ngày 2026-11-11 (ảnh chụp lỗi: `LienThuan04/log/Screenshot 2026-11-11 150933.png`). Test assert header này trong `tests/test_api_view*.py` — đổi header thì sửa test.

## Repo

- **`python api/app.py` báo `ModuleNotFoundError: No module named 'util'` trên Windows** → `api/util` (→ `../util/`) và `api/view.svg.py` (→ `view.py`) là git symlink; Windows checkout với `core.symlinks=false` biến chúng thành file text → chạy với `PYTHONPATH` = gốc repo: PowerShell `$env:PYTHONPATH='.'; python api/app.py`, bash `PYTHONPATH=. python api/app.py`. Giữ nguyên hai file symlink đó, đừng thay bằng bản copy (Vercel/Linux cần symlink).
- `api/callback.py` tự khởi tạo Firebase lúc import (đọc `FIREBASE`), không qua `util/firestore.py` → import module này mà thiếu env `FIREBASE` là crash, kể cả khi `TESTING=true`.
- `api/theme_dev.py` hỏng: gọi `make_svg(..., background_color)` nhưng biến chưa định nghĩa (dòng gán nhầm tên `rendered_data`) → `NameError`.
- CI (`ci.yml`) đặt `SPOTIFY_CLIENT_SECRET`, `REDIRECT_URI` nhưng code đọc `SPOTIFY_SECRET_ID` và tự suy `REDIRECT_URI` từ `BASE_URL`. Test vẫn qua vì mock; đừng lấy CI làm mẫu cấu hình env.
- `Dockerfile` dùng `python:3.11` trong khi `pyproject.toml` yêu cầu `>=3.12`.
- 5 template (`compact`, `default`, `karaoke`, `natemoo-re`, `novatorem`) bọc ảnh bìa trong `<a href="{}">` — placeholder kiểu `str.format` không bao giờ được điền, link chết (GitHub cũng không cho click bên trong SVG nên không ai thấy).
- `spotify.spotify-embed.html.j2` (dòng ~215): khi không có `progress_data`, thời gian còn lại được **bịa** từ độ dài tên bài (`song_name|length`).
- `compact`, `karaoke` vẫn chèn `css_bar` + keyframes `sound` nhưng không có thanh equalizer — code thừa, vô hại.

## Môi trường và graphify

- Preview Card Studio có thể render thành file HTML độc lập vì CSS/JS được Jinja include inline. Khi thêm asset builder, giữ cách include này; không đổi sang URL static nếu chưa kiểm route Vercel.
- Helper test `.pytest_cache/run_spotify_tests.py` từ phiên cũ có thể không truy cập được. Artifact mới ở `../.task-tools/spotify-readme-xlbb9rpk/`; script `verify_readme.py` chạy bản sao `source/` giải symlink, phải đồng bộ code vào bản sao trước khi chạy lại.
- Kiểm mạng ngày 2026-11-12: connector Vercel thiếu quyền project/team (403 lookup), urllib bị sandbox chặn socket WinError 10013 và CUA không có browser. Test Flask/Node local không xác nhận ảnh live hoặc clipboard/browser thực; ghi rõ giới hạn đó khi bàn giao.
- Windows sandbox có thể báo `fatal: detected dubious ownership in repository at '<repo>'`: dùng `git -c safe.directory=<đường dẫn tuyệt đối của repo> -C <repo> ...` cho từng lệnh.
- Graphify không có lệnh trần trên PATH; dùng `python -m graphify`. Graph local ở `graphify-out/`, bị gitignore; ảnh và lockfile bị loại qua `.graphifyignore`.
- PowerShell 5 có `$OutputEncoding` mặc định ASCII; khi pipe mã Python có tiếng Việt, đặt `$OutputEncoding = [System.Text.UTF8Encoding]::new()`. Đặt `$env:PYTHONIOENCODING='utf-8'` để in Unicode an toàn.
