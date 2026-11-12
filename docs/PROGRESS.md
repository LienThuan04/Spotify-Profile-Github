# PROGRESS — Spotify-Profile-Github

> Cập nhật: 2026-11-12 · Codex. HEAD trước phát hành `31bdbc7`.

## Đang làm

- Người dùng đã yêu cầu commit/push bản sửa và xác nhận **tạo tag + Release `V1.0.1` mới**, giữ `V1.0.0` hiện tại tại `31bdbc7`.
- Kiểm lại trước phát hành: **706 pytest pass in 2.40s**, **11 Node pass**, 105 SVG hợp lệ; remote master/tag V1.0.0 cùng `31bdbc74ab50af9c2928e9c3de32cabd9cb1f530`. Đang commit/push rồi tạo V1.0.1 tại HEAD mới.
- Git mạng trong sandbox lỗi `Failed to connect to github.com:443`; chạy ngoài sandbox đã đọc remote thành công. Connector đọc Release được nhưng không có tool tạo Release; `gh` không cài (`The term 'gh' is not recognized`), dùng Git và GitHub REST qua credential helper hiện có khi phát hành.

## Kết quả gần nhất

- Đã sửa 8 theme thiếu timeline/clock: default, compact, karaoke, natemoo-re, novatorem, apple, spotify-embed, spotify-mini. Cả 15 theme dùng chung thanh CSS + đồng hồ elapsed, dừng cùng cuối bài; recent tĩnh, offline ẩn, thiếu timing không chạy. Apple/Embed dùng thời gian thật, bên phải là tổng thời lượng.
- Mini cao 96px (offline 72px); 5 theme cũ thêm 33px khi có timeline. Chỉ thay make_svg/template/test, không đổi fetching/cache/Firestore hoặc symlink gốc. PROJECT/wiki/gotchas đã cập nhật; checkpoint cũ và chẩn đoán nằm trong `docs/memory/history.md`.
- RED tái hiện lỗi trước sửa. GREEN: **706 pytest pass in 2.24s**, **11 Node pass**; reviewer độc lập chạy thêm **602 test_api_view pass**, không có finding cần sửa. So AST: chỉ make_svg thay đổi; `git diff --check` qua.
- Preview: `graphify-out/timeline-review/index.html` + 105 SVG hợp lệ; runner `verify.py`, log `pytest.log`, `pytest.xml` cùng thư mục. Chạy `.venv/Scripts/python.exe graphify-out/timeline-review/verify.py` từ gốc repo để tạo snapshot giải symlink và kiểm lại. Sandbox chặn ghi snapshot nên lượt này chạy ngoài sandbox. JS: `node --test tests/test_builder.js`.
- Graph refresh: ban đầu `PermissionError: [Errno 13] Permission denied: 'graphify-out\\.rebuild.lock'`; chạy lại ngoài sandbox thành công **545 nodes / 772 edges / 38 communities**. Graph/artifact ignored, không đưa vào commit.
- Giới hạn: CUA `apps=[]`, `browsers=[]`; chưa xác nhận geometry/animation trong browser thật hoặc bản deploy. Đồng hồ dự đoán từ snapshot, pause/seek/đổi bài cần ảnh mới.

## Bước tiếp theo

- Commit các thay đổi timeline/docs/test, push master; tạo tag và Release V1.0.1 tại cùng commit, kiểm lại remote master/tag và release. Không sửa cấu hình deploy.

## Nhật ký

- 2026-11-12 · Codex · Người dùng duyệt push và chọn tạo V1.0.1 mới; xác minh remote V1.0.0/master ở 31bdbc7, kiểm lại 706 pytest/11 Node pass.
- 2026-11-12 · Codex · Hoàn tất timeline cho 15 theme theo yêu cầu sửa tất cả theme thiếu; 706 pytest/11 Node pass, 105 SVG, reviewer không finding; chưa commit/push.
