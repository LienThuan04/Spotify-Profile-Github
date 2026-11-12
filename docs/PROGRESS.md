# PROGRESS — Spotify-Profile-Github

> Cập nhật: 2026-11-12 · Codex. Ghi checkpoint ngay sau mỗi mốc.

## Đang làm

(trống) — hoàn tất chuyển đổi local theo yêu cầu; chưa push.

## Kết quả

- Repo mới: `https://github.com/LienThuan04/Spotify-Profile-Github.git`, branch `master`.
- Thương hiệu/URL đã đổi sang Spotify-Profile-Github của Lian Harman; README đứng tên Lian Harman, không còn mục Credits; pyproject có `authors`.
- `LICENSE` chỉ đứng tên Lian Harman (MIT 2026); giấy phép gốc Kittinan chuyển sang `THIRD_PARTY_NOTICES.md`. Theme API và template theme giữ nguyên.
- AGENTS/CLAUDE/GEMINI, PROJECT/PROGRESS, memory, skills nằm trong repo; `.gitignore` CRLF và `.graphifyignore` đã cấu hình.
- `api/requirements.txt` cài thành công vào `.venv`. Bộ test trên bản sao tạm giải tham chiếu đúng symlink Windows: **134 passed in 2.66s** (`TESTING=true`, `PYTHONPATH=.`).
- `python -m graphify update .`: exit 0; 407 nodes / 564 edges / 32 communities ở lần dựng đầu. Graph/report/HTML chỉ local, bị gitignore; lần refresh cuối có thể thêm node từ checkpoint.
- Đúng hai commit mới: root `883295e` (`Initial commit: Spotify-Profile-Github by Lian Harman`), sau đó `docs: add agent handoff docs, skills and memory` (HEAD). Branch/ref origin cũ đã xoá local; không push/gc. Tác giả theo git config hiện có; commit không có trailer Co-authored-by.
- Backup lịch sử cũ đã verify: `spotify-github-profile-full-history.bundle` ở đường dẫn ghi trong checkpoint workspace.

## Bước tiếp theo — người dùng thực hiện khi sẵn sàng

Đề xuất push từ gốc repo này (chưa thực hiện):

```sh
git push -u origin master
```

Nối lại project Vercel đang phục vụ `https://spotify-github-profile-lian-harman.vercel.app` với `LienThuan04/Spotify-Profile-Github`, branch `master`; giữ cấu hình biến môi trường hiện có, rồi kiểm tra deploy và card nhúng trên GitHub profile.

## Lỗi môi trường và cách kiểm tra

- Chạy trực tiếp `TESTING=true PYTHONPATH=. .venv/Scripts/python.exe -m pytest tests/` trên Windows: `api\view.svg.py:1: in <module>`, `view.py`, `E   NameError: name 'view' is not defined`; `ERROR tests/test_api_view_sg.py - NameError: name 'view' is not defined`, `1 error in 0.29s`.
- Nguyên nhân: `api/view.svg.py` và `api/util` là symlink git (mode `120000`), Windows checkout thành file text. Bản sao tạm `.task-tools/spotify-test` ở workspace giải tham chiếu đúng target (`view.py`, `../util/`) rồi chạy cùng suite. File và mode symlink trong repo giữ nguyên; trên Windows vẫn cần cách chạy này hoặc checkout hỗ trợ symlink thật.

## Nhật ký

- 2026-11-12 · Codex · Hoàn tất branding, credits, docs, kiểm thử, lịch sử mới và graph local; chưa push.
- 2026-11-12 · Codex · Root commit `883295e`, docs commit là HEAD; giữ đúng hai commit bằng amend commit docs khi chốt checkpoint.
