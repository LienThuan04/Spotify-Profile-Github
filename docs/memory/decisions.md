# Decisions — Spotify-Profile-Github

## 2026-11-12 — Tên tác giả hiển thị thống nhất

- Người dùng yêu cầu tên `LianHarman(LienThuan04)`; dùng đúng chuỗi này trong README, footer, metadata và LICENSE của bản hiện tại.
- Giấy phép upstream trong `THIRD_PARTY_NOTICES.md` giữ nguyên. Các URL/username GitHub, domain deploy và lịch sử commit giữ nguyên.

## 2026-11-12 — Repo độc lập của Lian Harman

- **Lý do:** người dùng yêu cầu tên sản phẩm/repo mới và lịch sử commit mới; giữ ghi công tác giả gốc.
- **Hệ quả:** origin là `https://github.com/LienThuan04/Spotify-Profile-Github.git`, branch `master`. README/LICENSE đứng tên tác giả hiện tại theo quy ước ở trên, giấy phép gốc upstream ở `THIRD_PARTY_NOTICES.md`; code giữ nguyên hành vi; commit không thêm `Co-authored-by`. Push theo yêu cầu người dùng.

## 2026-11-12 — Bộ nhớ và hướng dẫn nằm trong repo

- **Lý do:** nhiều agent cần bàn giao được cả sau khi clone repo riêng.
- **Hệ quả:** AGENTS.md là entry; CLAUDE.md/GEMINI.md trỏ về đó. Checkpoint ở `docs/PROGRESS.md`, reference ở `docs/PROJECT.md`, kiến thức bền ở `docs/memory/`, quy trình ở `docs/skills/`.

## 2026-11-12 — Graph chỉ index code và docs

- **Lý do:** ảnh/lockfile không giúp truy vấn symbol; graph là dữ liệu local có thể tạo lại.
- **Hệ quả:** `.graphifyignore` loại ảnh/lockfile; `/graphify-out` bị gitignore. Cập nhật bằng `python -m graphify update .`.

## 2026-11-11 — Cache card ở Vercel edge

- **Lý do:** GitHub camo timeout khi Vercel cold start.
- **Hệ quả:** `s-maxage=10, stale-while-revalidate=3600`. Presence/now playing có thể trễ vài chục giây.
