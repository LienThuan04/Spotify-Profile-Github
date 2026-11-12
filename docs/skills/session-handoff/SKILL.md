---
name: session-handoff
description: Resume or checkpoint work in this repository. Use at the start of every session, before stopping, and after finishing any task, so the next agent (Claude, Codex, Gemini, Antigravity) continues instead of starting over.
---

# Session handoff

`docs/PROGRESS.md` là **checkpoint** duy nhất của repo. Agent nào cũng có thể bị ngắt bất kỳ lúc nào, nên checkpoint phải luôn phản ánh đúng trạng thái *ngay bây giờ*.

## Khi bắt đầu phiên (resume)

1. Đọc `docs/PROGRESS.md` — mục **Đang làm** và **Bước tiếp theo**.
2. Trong repo hiện tại, chạy `git status --short` và `git log --oneline -5` rồi so với checkpoint. Lệch (có commit/thay đổi chưa ghi) → coi git là sự thật, cập nhật checkpoint trước khi làm tiếp.
3. Đọc `docs/PROJECT.md` của repo.

Xong khi: nói được trong một câu "đang ở đâu, bước tiếp theo là gì" mà không cần hỏi người dùng.

## Trong khi làm

Ghi checkpoint **ngay sau mỗi mốc** (một thay đổi đã chạy được, một commit, một phát hiện quan trọng) — không đợi cuối phiên, vì phiên có thể bị cắt.

## Khi dừng hoặc xong việc (checkpoint)

Cập nhật `docs/PROGRESS.md`:

1. **Đang làm**: việc dở dang + file đang sửa + lệnh để kiểm tra lại. Xong hết thì để `(trống)`.
2. **Bước tiếp theo**: hành động cụ thể đầu tiên, đủ để agent khác làm ngay.
3. **Nhật ký**: thêm 1 dòng trên cùng `YYYY-MM-DD · <agent> · <repo> · <việc đã làm> · <commit hash nếu có>`. Giữ tối đa ~20 dòng; dòng cũ hơn chuyển sang `docs/memory/history.md`.
4. Học được điều gì không hiển nhiên? → thêm vào `docs/memory/gotchas.md` (bẫy) hoặc `docs/memory/decisions.md` (quyết định + lý do).
5. Đổi cấu trúc code (thêm/xoá/đổi tên file)? → chạy skill `graphify-navigation` phần cập nhật graph.

Xong khi: một agent khác chỉ đọc `docs/PROGRESS.md` là biết làm tiếp từ đâu.
