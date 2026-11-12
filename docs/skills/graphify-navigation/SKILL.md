---
name: graphify-navigation
description: Find files, symbols and relationships within this repo via the graphify knowledge graph in graphify-out/. Use before opening files to answer "where is X / what calls Y / how does A reach B", and after adding, removing or renaming code files to refresh the graph.
---

# Điều hướng bằng graphify

Graph nằm ở `graphify-out/` (gốc repo):

| File | Dùng để |
|---|---|
| `GRAPH_REPORT.md` | Đọc đầu tiên: god nodes, cộng đồng (communities), kết nối bất ngờ. |
| `graph.json` | Dữ liệu thô (NetworkX node-link); mỗi node có `source_file`, `source_location`. |
| `graph.html` | Mở bằng trình duyệt để xem trực quan. |

## Tra cứu

Lệnh `graphify` không có trên PATH; luôn gọi qua Python có cài graphify:

```sh
python -m graphify query "spotify token refresh" --budget 2000
python -m graphify query "spotify token refresh" --dfs        # lần theo một đường cụ thể
python -m graphify path "renderCard()" "fetchUserBanner()"     # đường ngắn nhất giữa 2 node
python -m graphify explain "make_svg()"                        # node + hàng xóm
```

- Chạy từ gốc repo này. Nếu `python` không import được graphify, dùng đường dẫn trong `graphify-out/.graphify_python`.
- Tên node là **label** của nó: hàm có hậu tố `()` (`make_svg()`), file là tên file (`view.py`), method có dấu chấm đầu (`.solve()`).
- `query` mặc định cắt kết quả theo budget token; thấy dòng `TRUNCATED` thì tăng `--budget` hoặc hỏi hẹp hơn.

Kết quả trả về `source_file` + `source_location` (dạng `L123`) → mở đúng dòng đó thay vì đọc cả repo. Graph không thấy được: nội dung ảnh SVG (bị `.graphifyignore` loại), giá trị env, hành vi runtime — với những thứ đó đọc file trực tiếp.

## Cập nhật graph

- **Mặc định** (agent nào cũng chạy được, không tốn LLM): `python -m graphify update .` — trích xuất lại code + cấu trúc heading của file `.md`, giữ nguyên node ngữ nghĩa cũ, tự backup bản trước vào `graphify-out/<ngày>/`.
- Muốn bổ sung quan hệ ngữ nghĩa sâu cho README/template: có thể chạy `/graphify . --update` trong Claude Code. Đây là bước tùy chọn; `python -m graphify update .` đủ để cập nhật code và heading.
- Graph từ chối ghi khi số node giảm (bảo vệ chống mất dữ liệu). Nếu thật sự đã xoá file: thêm `--force`.
- Muốn graph bỏ qua thêm loại file: sửa `.graphifyignore` ở gốc (cú pháp gitignore).

Xong khi: lệnh chạy không lỗi và `GRAPH_REPORT.md` có ngày sửa mới.
