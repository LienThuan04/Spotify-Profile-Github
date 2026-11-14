# Gotchas — Spotify-SPARK

Triệu chứng → nguyên nhân → cách xử lý. Ghi thêm sau khi xác minh; bỏ mục đã hết hiệu lực.

## Card trên GitHub

- Đồng hồ CSS phải dùng delay âm có cả milliseconds: mốc 59.8s chỉ còn 0.2s tới 1:00. Đồng hồ và thanh cùng mốc dừng, final time giữ tĩnh. Test timing/markup không xác nhận được clipping/baseline/animation thực trong browser; luôn ghi rõ giới hạn và kiểm preview trước khi khẳng định hiển thị chuẩn.
- **Card Spotify/Discord hiện ảnh vỡ trên trang profile** → GitHub tải ảnh qua proxy `camo.githubusercontent.com`, bỏ cuộc nếu server phản hồi chậm (cold start Vercel 4s+) → đặt header `Cache-Control: public, ..., s-maxage=..., stale-while-revalidate=3600` để Vercel edge trả bản cache. Đã áp dụng cho cả 2 repo ngày 2026-11-11 (ảnh chụp lỗi: `LienThuan04/log/Screenshot 2026-11-11 150933.png`). Test assert header này trong `tests/test_api_view*.py` — đổi header thì sửa test.
- **Đo lại 2026-11-14, cùng URL trong `LienThuan04/README.md`:** code lúc đó gửi `public, max-age=0, s-maxage=10, stale-while-revalidate=86400`, nhưng response tới client/Camo chỉ còn `Cache-Control: public, max-age=0` (Vercel nuốt `s-maxage` và `stale-while-revalidate`). `X-Vercel-Cache`: MISS **4744 ms**, HIT/STALE **190–513 ms**. Ảnh README nằm trong `<a href="...&redirect=true">`, alt `Spotify Now Playing` — Camo bỏ cuộc thì chỉ còn chữ link đó (đúng ảnh 11/11). `max-age=0` khiến Camo không giữ ảnh. Spotify HTTP trong `util/spotify.py` không có timeout; đang phát thì còn tải ảnh bìa (timeout 10s).
- **Cách sửa (chưa deploy):** `apply_card_cache()` trong `api/view.py` tách hai header. `Cache-Control: public, max-age=60` là thứ Camo thấy và giữ ảnh khoảng một phút. `Vercel-CDN-Cache-Control: public, s-maxage=60, stale-while-revalidate=86400` chỉ cho CDN, để lần Camo tải lại thường là HIT/STALE dưới 1 giây chứ không phải cold start. Đừng gộp `s-maxage` vào `Cache-Control` nữa. Lần đầu hoàn toàn lạnh vẫn có thể vượt 4 giây một lần; sau đó cache giữ. Test: `TESTING=true pytest tests/test_api_view.py` (26 case lọc cache/offline/now_playing qua). `tests/test_api_view_sg.py` trên Windows vẫn lỗi symlink `view.svg.py` như cũ, không do header.

## Repo

- Card Studio dùng `legend` float full-width: clearance phải áp dụng cho mọi sibling (`legend~*`), vì sibling đầu `equalizer-field` bị ẩn khi chọn layout cũ. Selector `legend+*` khiến các ô màu/mode bị ép sang mép phải. Grid màu dùng auto-fit để một màu không để trống nửa hàng.
- **`python api/app.py` báo `ModuleNotFoundError: No module named 'util'` trên Windows** → `api/util` (→ `../util/`) và `api/view.svg.py` (→ `view.py`) là git symlink; Windows checkout với `core.symlinks=false` biến chúng thành file text → chạy với `PYTHONPATH` = gốc repo: PowerShell `$env:PYTHONPATH='.'; python api/app.py`, bash `PYTHONPATH=. python api/app.py`. Giữ nguyên hai file symlink đó, đừng thay bằng bản copy (Vercel/Linux cần symlink).
- `api/callback.py` tự khởi tạo Firebase lúc import (đọc `FIREBASE`), không qua `util/firestore.py` → import module này mà thiếu env `FIREBASE` là crash, kể cả khi `TESTING=true`.
- `api/theme_dev.py` hỏng: gọi `make_svg(..., background_color)` nhưng biến chưa định nghĩa (dòng gán nhầm tên `rendered_data`) → `NameError`.
- CI (`ci.yml`) đặt `SPOTIFY_CLIENT_SECRET`, `REDIRECT_URI` nhưng code đọc `SPOTIFY_SECRET_ID` và tự suy `REDIRECT_URI` từ `BASE_URL`. Test vẫn qua vì mock; đừng lấy CI làm mẫu cấu hình env.
- `Dockerfile` dùng `python:3.11` trong khi `pyproject.toml` yêu cầu `>=3.12`.
- 5 template (`compact`, `default`, `karaoke`, `natemoo-re`, `novatorem`) bọc ảnh bìa trong `<a href="{}">` — placeholder kiểu `str.format` không bao giờ được điền, link chết (GitHub cũng không cho click bên trong SVG nên không ai thấy).
- All 15 themes share timeline macros. Apple/Embed no longer use sample timestamps or derive time from song names; missing timing stays at a static 0:00. Import `timeline_styles()` for classic themes; `styles()` also applies Spotify layout and equalizer styles.
- `compact`, `karaoke` vẫn chèn `css_bar` + keyframes `sound` nhưng không có thanh equalizer — code thừa, vô hại.

## Môi trường và graphify

- Nếu Git bị chặn mạng nhưng connector GitHub hoạt động: upload blob riêng rồi create_tree theo SHA, kiểm tree khớp `git write-tree`, tạo commit và update_ref fast-forward có expected SHA. API date có thể hiển thị UTC dù raw commit dùng `+0700`; khi nhập commit local phải kiểm SHA object khớp tuyệt đối trước khi update-ref, không tự giả định `+0000` hoặc force-push.
- Preview Card Studio có thể render thành file HTML độc lập vì CSS/JS được Jinja include inline. Khi thêm asset builder, giữ cách include này; không đổi sang URL static nếu chưa kiểm route Vercel.
- Helper test `.pytest_cache/run_spotify_tests.py` từ phiên cũ có thể không truy cập được. Artifact mới ở `../.task-tools/spotify-readme-xlbb9rpk/`; script `verify_readme.py` chạy bản sao `source/` giải symlink, phải đồng bộ code vào bản sao trước khi chạy lại.
- Kiểm mạng ngày 2026-11-12: connector Vercel thiếu quyền project/team (403 lookup), urllib bị sandbox chặn socket WinError 10013 và CUA không có browser. Test Flask/Node local không xác nhận ảnh live hoặc clipboard/browser thực; ghi rõ giới hạn đó khi bàn giao.
- Windows sandbox có thể báo `fatal: detected dubious ownership in repository at '<repo>'`: dùng `git -c safe.directory=<đường dẫn tuyệt đối của repo> -C <repo> ...` cho từng lệnh.
- Graphify không có lệnh trần trên PATH; dùng `python -m graphify`. Graph local ở `graphify-out/`, bị gitignore; ảnh và lockfile bị loại qua `.graphifyignore`.
- PowerShell 5 có `$OutputEncoding` mặc định ASCII; khi pipe mã Python có tiếng Việt, đặt `$OutputEncoding = [System.Text.UTF8Encoding]::new()`. Đặt `$env:PYTHONIOENCODING='utf-8'` để in Unicode an toàn.
