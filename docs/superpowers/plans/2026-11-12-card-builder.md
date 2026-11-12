# Spotify card builder Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for inline execution. Continue the current local work; do not commit or push.

> Cập nhật sau triển khai: người dùng đã yêu cầu commit/push ngày 2026-11-12. Chỉ thị mới này thay thế giới hạn commit/push của kế hoạch ban đầu; Discord/profile vẫn giữ nguyên.

**Goal:** Xây lại trang tạo Markdown/link nhúng để người dùng chọn đầy đủ các theme và tùy chỉnh mới.

**Architecture:** Giữ callback OAuth hiện có, thay template bằng giao diện responsive hai cột. CSS/JS đặt trong partial Jinja và include inline để tương thích cả Vercel và Flask mà không thêm route hay CDN.

**Tech Stack:** Flask/Jinja, CSS, JavaScript thuần, pytest và Node test runner.

**Spec:** Yêu cầu người dùng ngày 2026-11-12: “sửa luôn trang giao diện Markdown Code tạo link nhúng … đập xây lại hết … để người dùng có các tùy chỉnh mới”. Các lựa chọn trình bày dưới đây do Codex đề xuất để thực hiện yêu cầu ngay.

## Global Constraints

- Giữ OAuth, Firestore, Spotify fetching và 10 template card hiện có.
- Đủ 10 theme, 9 eq; các tùy chọn chỉ gửi khi theme hỗ trợ.
- Giao diện tối theo Spotify, responsive, label/focus/keyboard rõ ràng.
- Có live preview và mã Markdown/HTML/URL, copy có phản hồi thành công/thất bại.
- Không commit/push; không sửa Discord hoặc profile.

## Review Focus

- Theme switching: giữ giá trị người dùng nhưng không phát tham số không được hỗ trợ.
- URL/base URL/uid có ký tự đặc biệt: URLSearchParams và Jinja tojson bảo toàn giá trị.
- Open in Spotify: redirect chỉ ở link click, không nằm trong src ảnh.
- Clipboard bị từ chối và preview lỗi: trạng thái rõ ràng, vẫn lấy được mã.
- Cover tắt khi auto color bật: không yêu cầu trích màu khi không tải ảnh bìa.

### Task 1: Trang builder và URL/code thực

**Files:** `api/templates/callback.html.j2`, `api/templates/_builder/styles.css`, `api/templates/_builder/builder.js`, `tests/test_builder.js`, `tests/test_builder_template.py`.

**Interfaces:** `buildEmbed(config, state)` trả imageUrl/linkUrl/markdown/html; `getThemeFeatures(theme)` trả các khả năng của theme; `mount(document, config)` nối controls với preview/code/copy.

- [x] Viết test thực thi JS: theme/eq, màu mặc định/custom, bo góc, booleans, mode, redirect, UID encoding và cover/auto color.
- [x] Chạy Node test để thấy fail do module builder chưa có.
- [x] Dựng template/partial: panel tùy chỉnh, preview, tabs code, copy, reset; không thêm dependency.
- [x] Chạy test JS và render Jinja bằng pytest; kiểm cấu hình được JSON escape và labels không trỏ ID thiếu.

### Task 2: Kiểm đầy đủ và bàn giao

**Files:** README, docs/PROJECT.md, docs/PROGRESS.md, workspace docs/PROGRESS.md.

- [x] Chạy suite pytest trên bản sao giải symlink Windows, Node tests và diff check.
- [x] Kiểm URL mới qua Flask với dữ liệu giả playing/recent/offline; không gọi Spotify/Firestore thật.
- [x] Đọc lại diff và kiểm responsive CSS/keyboard/error states; ghi hạn chế browser/live hiện tại.
- [x] Refresh graph, ghi checkpoint sau mỗi mốc; giữ thay đổi local chờ người dùng.

## Kết quả thực hiện

- Task 1: complete — Node 11/11, pytest 215/215; case preview error RED→GREEN.
- Task 2: URL integration 41×3 = 123 SVG, README 31×3 = 93 SVG; diff check qua.
- Graph cuối: 510 nodes / 720 edges / 36 communities; graph chỉ local.
- Final review: reviewer độc lập không có finding cần sửa; browser/live/clipboard/keyboard thực chưa kiểm được do giới hạn môi trường. Thay đổi vẫn local theo yêu cầu không commit/push.
