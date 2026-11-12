# AGENTS.md — Spotify-Profile-Github

Spotify-Profile-Github của Lian Harman (`LienThuan04`). API sinh card Spotify now playing bằng Python, Flask và Firestore.
Repo: `https://github.com/LienThuan04/Spotify-Profile-Github`. Branch: `master`.

## Bắt đầu phiên

1. Đọc `docs/PROGRESS.md`, rồi làm theo `docs/skills/session-handoff/SKILL.md` để đối chiếu với git.
2. Đọc `docs/PROJECT.md` trước khi sửa code hoặc cấu hình.
3. Cập nhật `docs/PROGRESS.md` ngay sau mỗi mốc, kể cả lỗi và việc chưa xong.

## Skills

| Skill | Đọc khi |
|---|---|
| `docs/skills/session-handoff/SKILL.md` | Bắt đầu phiên, xong một việc, hoặc dừng phiên. |
| `docs/skills/graphify-navigation/SKILL.md` | Tìm file/symbol/quan hệ; cập nhật graph sau thay đổi cấu trúc. |
| `docs/skills/spotify-card/SKILL.md` | Sửa theme, tham số, token/Firestore hoặc chạy Spotify local. |

## Bộ nhớ

- Khi gặp lỗi lạ, đọc `docs/memory/gotchas.md`; ghi nguyên nhân và cách xử lý sau khi xác minh.
- Trước khi đổi quy ước, đọc `docs/memory/decisions.md`; ghi quyết định mới và lý do.
- Nhật ký cũ chuyển sang `docs/memory/history.md` khi checkpoint dài quá ~20 dòng.

## Quy tắc

- Giao tiếp và viết tài liệu bàn giao bằng tiếng Việt.
- Với câu hỏi file/symbol/quan hệ, chạy `python -m graphify query "<câu hỏi>"` (hoặc `path` / `explain`) trước khi grep/mở code, rồi mở đúng `source_file:source_location`. Nếu graph thiếu hoặc lệnh lỗi, ghi lỗi trong checkpoint rồi đọc trực tiếp các file liên quan.
- Chạy git trong repo này (`git -C <đường dẫn repo> ...` khi đứng ngoài repo).
- Commit/push chỉ khi người dùng yêu cầu; commit không thêm `Co-authored-by`.
- Mọi chỗ hiển thị (README, LICENSE, trang, metadata) đứng tên Lian Harman. Giấy phép MIT gốc của Kittinan nằm ở `THIRD_PARTY_NOTICES.md` — giữ file đó (điều kiện của MIT).
- Code giữ nguyên hành vi như bản gốc; chỉ sửa logic khi người dùng yêu cầu.
