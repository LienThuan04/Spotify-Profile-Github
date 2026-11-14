# Decisions — Spotify-Profile-Github

## 2026-11-14 — Split the card cache headers

- GitHub Camo only reads `Cache-Control`. Putting `s-maxage` on that header made Vercel strip it and send `max-age=0`, so every README view refetched the SVG and a cold start (~5s) became a broken image link.
- `apply_card_cache()` now sets `Cache-Control: public, max-age=60` for Camo and `Vercel-CDN-Cache-Control: public, s-maxage=60, stale-while-revalidate=86400` for the Vercel CDN only. Do not put `s-maxage` back on `Cache-Control`. The 2026-11-11 cache note below is superseded.

## 2026-11-12 — Project language

- The user requested English for project content. Write new documentation, handoffs, UI copy, and release notes in English; continue communicating with the user in Vietnamese. The language rule in AGENTS.md records this preference.

## 2026-11-12 — Timelines for every theme

- The user requested progress bars and elapsed clocks for every remaining theme. All 15 themes share CSS timeline macros, project playback from the Spotify snapshot, and stop at the track duration. JavaScript, fetching, and caching remain unchanged.
- Apple/Embed show real elapsed and total times instead of sample values; missing timing stays static. Mini grows to 96px and five classic themes gain 33px while displaying a timeline. Offline cards retain their previous heights.

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
- **Hệ quả:** lúc đó `s-maxage=10, stale-while-revalidate=3600`. Đã bị thay bởi mục 2026-11-14: Camo không thấy `s-maxage` trên `Cache-Control`.
