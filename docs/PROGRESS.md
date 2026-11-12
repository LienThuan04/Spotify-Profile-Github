# PROGRESS — Spotify-Profile-Github

> Cập nhật: 2026-11-12 · Codex. Ghi checkpoint ngay sau mỗi mốc.

## Đang làm

(trống) — Mục 1–7 bên dưới đã hoàn tất; chờ Claude duyệt ảnh trong thư mục review. Không commit/push.

## Đã hoàn tất — 3 theme kiểu Spotify + 6 kiểu sóng nhạc (người dùng đã duyệt 2026-11-12)

Tham chiếu bắt buộc đọc: `DESIGN-spotify.md` (gốc repo, file người dùng thêm — giữ nguyên, không commit), mockup đã duyệt `D:\Coding\profileLienThuan04\.superpowers\brainstorm\1305-1794455217\content\card-layout.html` (bố cục A/B/C) và `...\eq-styles.html` (6 kiểu sóng nhạc). Bám sát mockup.

Phạm vi: chỉ thêm mới. 7 theme cũ (kể cả `default`) giữ nguyên từng byte; logic lấy dữ liệu Spotify giữ nguyên.

- [x] 1. **3 template mới** `api/templates/spotify.<theme>.html.j2`, cùng kiểu SVG + `foreignObject` như template cũ, **không JavaScript**, chỉ CSS:
  - `spotify-card` 400×200 (mockup A) · `spotify-bar` 400×112 (mockup B) · `spotify-album` rộng 240, cao tính theo nội dung (mockup C; không ảnh bìa thì thấp lại).
  - Màu/chữ theo DESIGN: nền `#{{background_color}}` (mặc định 121212), chữ `#fff`, phụ `#b3b3b3`, track `#4d4d4d`, fill `#fff`, logo Spotify SVG inline `#1ed760`; font `"Helvetica Neue", Helvetica, Arial, sans-serif`; ảnh bìa bo 6px (bar 4px) + bóng `rgba(0,0,0,.5) 0 8px 24px`; card bo `{{border_radius}}px`. Không dùng `<a href="{}">`.
  - Nhãn trên cùng = `title_text` viết hoa, letter-spacing 1.4px ("NOW PLAYING" / "RECENTLY PLAYED" / "NOT PLAYING").
  - Tên bài/nghệ sĩ dài → `text-overflow: ellipsis`. `cover_image=false` → bỏ ảnh bìa, bố cục co lại hợp lý.
  - Trạng thái: đang phát → sóng nhạc chạy + tiến trình chạy; bài gần đây → sóng nhạc đứng yên, tiến trình 0 và `0:00` / tổng; offline → ẩn sóng nhạc và tiến trình.
- [x] 2. **Sóng nhạc** tham số mới `eq_style` ∈ `bars` (mặc định) | `spectrum` | `mirror` | `wave` | `pulse` | `none`; giá trị lạ → `bars`. Màu = `bar_color` (hoặc màu ảnh bìa khi `bar_color_cover=true`, logic cũ). Với 3 theme mới, nếu link không có `bar_color` thì mặc định `1ed760`. Thời lượng ngẫu nhiên cho từng thanh (spectrum/mirror) sinh ở Python/Jinja, không JS.
- [x] 3. **`api/view.py`**: đọc `eq_style` trong `catch_all`; `make_svg(..., eq_style="bars")` thêm tham số cuối có mặc định (lời gọi cũ vẫn chạy); chiều cao + `num_bar` cho 3 theme trong `make_svg`; thêm 3 theme vào danh sách nhận `progress_data`; truyền thêm `total_time` (= `format_time_ms(duration_ms)`) và `eq_style` vào template. Tiến trình: CSS animation từ `progress_percentage`% tới 100% trong số giây còn lại, `linear forwards`; giờ hiển thị tĩnh.
- [x] 4. **Trang tạo link** `api/templates/callback.html.j2`: thêm 3 theme vào `#theme-select`; thêm ô chọn `eq_style` (6 lựa chọn) chỉ hiện với 3 theme mới; `updateUrl()` thêm `eq_style`; ô màu sóng nhạc hiện với 3 theme mới.
- [x] 5. **Test** (`tests/test_api_view.py`): chiều cao 3 theme; `eq_style` hợp lệ/lạ; mỗi `eq_style` render ra đúng class; `bar_color` mặc định `1ed760` cho theme mới; theme mới nhận `progress_data`; test cũ vẫn xanh. Chạy test trên Windows theo cách trong mục "Lỗi môi trường" ở dưới (bản sao tạm giải symlink).
- [x] 6. **Ảnh minh hoạ + README**: script sinh `img/spotify-card.svg`, `img/spotify-bar.svg`, `img/spotify-album.svg` bằng `make_svg` với dữ liệu mẫu (bài "Time To Pretend" — "Lazer Boomerang", ảnh bìa gradient tạo bằng Pillow). README: thêm 3 theme vào bảng + ảnh, dòng `eq_style` vào bảng tham số.
- [x] 7. Sinh thêm vào `D:\Coding\profileLienThuan04\.superpowers\brainstorm\1305-1794455217\content\review\` một SVG cho mỗi (theme × trạng thái đang phát) và mỗi `eq_style` trên `spotify-card`, để Claude kiểm tra bằng mắt. **Không commit, không push.**

### Checkpoint triển khai 2026-11-12

- Đầu phiên: HEAD `2cd1a79`, root `64f5304`; chỉ có `docs/PROGRESS.md` đã sửa và `DESIGN-spotify.md` chưa tracked. Đã đối chiếu git, đọc PROJECT, các skill repo, DESIGN và cả hai mockup; không commit/push.
- Mục 1: 3 template + macro dùng chung; 9 lượt render (3 theme × 3 trạng thái) qua XML, không script/link placeholder, offline ẩn player.
- Mục 2: 6 kiểu sóng CSS; giá trị lạ về bars; spectrum 40/mirror 28 thanh có thời lượng Jinja ngẫu nhiên. 7 lượt render eq/fallback hợp lệ.
- Mục 3: nối `eq_style`, mặc định xanh mới, progress/total/giây còn lại; kiểm render và endpoint offline qua. Album 350px có bìa / 128px không bìa, offline giảm 33px. Item=None dùng nhãn offline chỉ với theme mới; không sửa lấy dữ liệu.
- Quyết định: nhãn trạng thái trên cả ba theme; tên bài màu trắng theo yêu cầu (mockup B màu xanh). Làm trực tiếp trong repo, bổ sung test ở mục 5 theo thứ tự người dùng yêu cầu.
- Mục 4: trang tạo link có 3 theme và 6 eq, eq chỉ hiện với theme mới; màu theo mặc định theme và giữ màu custom.
- Mục 5: bản sao Windows giải symlink trong `.pytest_cache/spotify-test` chạy **204 passed in 1.19s** (134 cũ + 70 mới). Chạy lại: `.venv/Scripts/python.exe .pytest_cache/run_spotify_tests.py`; log `.pytest_cache/spotify-tests.log`. Symlink gốc giữ nguyên.
- Mục 6: `scripts/generate_spotify_examples.py` sinh 3 SVG README qua make_svg, bài Time To Pretend / Lazer Boomerang và gradient Pillow; README có ảnh, theme, eq_style/màu mới. XML/kích thước đã kiểm.
- Mục 7: 18 SVG tại thư mục review ở trên (3 theme × playing/recent/offline/no-cover + 6 eq trên spotify-card); tất cả là XML hợp lệ, không script.
- Lỗi kiểm trực quan: `cua.createBrowserTab('iab', 'http://127.0.0.1:5018/_preview', {visible:false})` trả chính xác `Browser is not available: iab`; inventory apps/browsers rỗng. Chưa thể xác nhận bằng ảnh chụp trình duyệt. Server preview đã dừng.
- Kiểm callback: chạy script JS thực bằng Node với DOM adapter, 18 ca URL/Markdown/HTML (3 theme × 6 eq), ẩn/hiện, đổi theme cũ, mặc định/custom màu đều qua. `git diff --check` qua.
- SHA-256 xác nhận 7 template cũ, DESIGN và util/spotify.py nguyên byte; 6 hàm fetching/cache/image trong view.py giữ nguyên source so với HEAD.
- Lỗi ghi checkpoint: PowerShell pipe dùng ASCII khiến literal heading tiếng Việt trong Python thành `?`, nên các phép replace thêm ghi chú không khớp (không có exception); checkbox ASCII vẫn lưu đúng sau từng mục. Đã khôi phục ghi chú bằng apply_patch Unicode; từ đây dùng apply_patch hoặc đặt `$OutputEncoding` UTF-8 như gotchas đã chỉ dẫn.
- Reviewer độc lập đã đọc cả file untracked: không có finding Critical/Important/Minor. Không gọi Spotify/Firestore thật vì fetching giữ nguyên; render browser/GitHub Camo chưa kiểm bằng mắt.
- Lỗi refresh graph: `python -m graphify update .` exit 1 tại `graphify/watch.py:224`, `fh = open(lock_path, "a+", encoding="utf-8")` → `PermissionError: [Errno 13] Permission denied: 'graphify-out\\.rebuild.lock'`. Log đầy đủ: `.pytest_cache/spotify-graph-update.log`; graph vẫn là bản cũ 409 nodes / 565 edges, chưa chứa symbol mới.
- Kiểm lock sau lỗi: `Get-Item : Cannot find path 'D:\Coding\profileLienThuan04\spotify-github-profile\graphify-out\.rebuild.lock' because it does not exist.` và `Get-Acl : Cannot find path 'D:\Coding\profileLienThuan04\spotify-github-profile\graphify-out\.rebuild.lock' because it does not exist.` Không sửa quyền hoặc file ngoài phạm vi.
- Bàn giao: đã hoàn tất 1–7; không commit/push, không sửa DESIGN; ngoài repo chỉ ghi 18 SVG vào đúng review. Hạn chế còn lại: chưa kiểm hình bằng browser/GitHub, graph refresh lỗi như trên.

## Kết quả

- Thêm 3 theme Spotify, 6 eq CSS, trang tạo link, 70 case kiểm thử và script/ảnh mẫu; tổng **204 tests passed**. Checklist và lỗi phiên hiện tại ở trên.
- Repo mới: `https://github.com/LienThuan04/Spotify-Profile-Github.git`, branch `master`.
- Thương hiệu/URL đã đổi sang Spotify-Profile-Github của Lian Harman; README đứng tên Lian Harman, không còn mục Credits; pyproject có `authors`.
- `LICENSE` chỉ đứng tên Lian Harman (MIT 2026); giấy phép gốc Kittinan chuyển sang `THIRD_PARTY_NOTICES.md`. Theme API và template theme giữ nguyên.
- AGENTS/CLAUDE/GEMINI, PROJECT/PROGRESS, memory, skills nằm trong repo; `.gitignore` CRLF và `.graphifyignore` đã cấu hình.
- `api/requirements.txt` cài thành công vào `.venv`. Bộ test trên bản sao tạm giải tham chiếu đúng symlink Windows: **134 passed in 2.66s** (`TESTING=true`, `PYTHONPATH=.`).
- `python -m graphify update .`: exit 0; 407 nodes / 564 edges / 32 communities ở lần dựng đầu. Graph/report/HTML chỉ local, bị gitignore; lần refresh cuối có thể thêm node từ checkpoint.
- Đúng hai commit hiện có: root `64f5304` (`Initial commit: Spotify-Profile-Github by Lian Harman`), sau đó `2cd1a79` (`docs: add agent handoff docs, skills and memory`, HEAD). Thay đổi theme phiên này chưa commit. Branch/ref origin cũ đã xoá local; không push/gc. Tác giả theo git config hiện có; commit không có trailer Co-authored-by.
- Backup lịch sử cũ đã verify: `spotify-github-profile-full-history.bundle` ở đường dẫn ghi trong checkpoint workspace.

## Bước tiếp theo

- Claude mở SVG trong `D:\Coding\profileLienThuan04\.superpowers\brainstorm\1305-1794455217\content\review\`, đối chiếu hai mockup ở thư mục cha; đặc biệt kiểm ellipsis, sóng spectrum/mirror/wave, trạng thái recent/offline và bản không bìa.
- Sinh lại ảnh: `.venv/Scripts/python.exe scripts/generate_spotify_examples.py --review-dir "D:\Coding\profileLienThuan04\.superpowers\brainstorm\1305-1794455217\content\review"`.
- Nếu sửa tiếp: đọc phần checkpoint, chạy lại test Windows bằng `.venv/Scripts/python.exe .pytest_cache/run_spotify_tests.py`; thử refresh graph khi môi trường cho ghi `.rebuild.lock`. Không commit/push nếu chưa được yêu cầu.

Việc deploy để sau khi người dùng yêu cầu: nối project Vercel đang phục vụ `https://spotify-github-profile-lian-harman.vercel.app` với `LienThuan04/Spotify-Profile-Github`, branch `master`; giữ biến môi trường hiện có.

## Lỗi môi trường và cách kiểm tra

- Chạy trực tiếp `TESTING=true PYTHONPATH=. .venv/Scripts/python.exe -m pytest tests/` trên Windows: `api\view.svg.py:1: in <module>`, `view.py`, `E   NameError: name 'view' is not defined`; `ERROR tests/test_api_view_sg.py - NameError: name 'view' is not defined`, `1 error in 0.29s`.
- Nguyên nhân: `api/view.svg.py` và `api/util` là symlink git (mode `120000`), Windows checkout thành file text. Bản sao tạm `.task-tools/spotify-test` ở workspace giải tham chiếu đúng target (`view.py`, `../util/`) rồi chạy cùng suite. File và mode symlink trong repo giữ nguyên; trên Windows vẫn cần cách chạy này hoặc checkout hỗ trợ symlink thật.
- Phiên theme hiện tại dùng bản sao **bên trong repo** `.pytest_cache/spotify-test` và script `.pytest_cache/run_spotify_tests.py`, không dùng đường dẫn workspace bên ngoài. Nếu cache bị xóa, copy `api/`, `util/`, `tests/`, `pyproject.toml` vào thư mục tạm trong repo, thay `api/view.svg.py` bằng bản copy `api/view.py`, thay `api/util` bằng bản copy `util/`; chạy `.venv/Scripts/python.exe -m pytest tests/` từ bản sao với `TESTING=true`, `PYTHONPATH` trỏ đến bản sao. Không sửa symlink gốc.

## Nhật ký

- 2026-11-12 · Claude Code · Sửa theo duyệt: offline có ô ảnh xám (spotify-card/bar), chữ offline xuống dòng ở cả 3 theme, album offline cao 114 (có bìa 336). 204 test pass, 7 theme cũ không đổi. Commit `feat`. Kế tiếp: mockup sóng giả 3D (CSS) chờ người dùng duyệt; three.js không chạy được trong ảnh SVG của GitHub.
- 2026-11-12 · Codex · Spotify-Profile-Github · Hoàn tất mục 1–7: 3 theme, 6 eq, callback, 204 tests qua, 3 SVG README + 18 SVG review; giữ nguyên theme cũ/fetching; lỗi browser/graph đã ghi; chưa commit/push.
- 2026-11-12 · Codex · Hoàn tất branding, credits, docs, kiểm thử, lịch sử mới và graph local; chưa push.
- 2026-11-12 · Codex · Lịch sử trước phiên theme: root `64f5304`, docs `2cd1a79`; phiên theme không amend/commit.
