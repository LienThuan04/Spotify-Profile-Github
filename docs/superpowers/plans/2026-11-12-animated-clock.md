# Animated Spotify clock Implementation Plan

> Thực hiện local theo yêu cầu sửa của người dùng; chưa stage/commit/push.

> Cập nhật sau kiểm thử: người dùng đã duyệt push đồng hồ và yêu cầu dừng sau khi xong để chờ hướng tiếp theo. Chỉ thị mới thay thế giới hạn commit/push ban đầu, giữ README profile và .gitignore người dùng ngoài commit.

**Goal:** Số thời gian hiện tại trên spotify-card/bar/album tăng đồng bộ với thanh tiến độ.

**Architecture:** CSS steps() dịch các dải số phút/hàng chục giây/hàng đơn vị giây. Delay âm đặt đúng pha từ progress_ms, giữ phần milliseconds; cùng thời điểm thanh kết thúc, chuyển sang text thời lượng cuối. Không JavaScript trong SVG.

**Scope:** Chỉ ba theme mới dùng macro shared và dữ liệu đồng hồ từ make_svg. Giữ nguyên 7 template cũ, fetching/cache/OAuth, README profile đang chờ duyệt và .gitignore của người dùng.

**Hành vi:** Đang phát và có progress/duration hợp lệ thì chạy. Recent ở 0:00, offline ẩn player, thiếu dữ liệu/đã hết bài thì tĩnh. Tổng thời lượng bên phải không đổi. Clock và bar vẫn là dự đoán từ snapshot ảnh, không biết pause/seek/đổi bài cho tới khi nhận ảnh mới.

**Tests:** Render SVG thật; đánh giá frame từ cấu hình CSS steps()/duration/delay và các hàng số được phát ra, với expected time viết tay. Đây là kiểm mô hình timing/markup, không thay cho browser QA.

- [x] RED: test cả 3 theme ở 3:16→3:17, 0:59.8→1:00 đúng sau 0.2s, 9:59→10:00, và dừng cuối bài.
- [x] RED: recent/offline/missing/zero/overrun không có clock chạy; bài dài không sinh một frame mỗi giây.
- [x] GREEN: calculate_clock_data, truyền context, macro elapsed clock và CSS reels.
- [x] Kiểm full pytest trên snapshot giải symlink, Node tests, SVG/XML và 7 template cũ/fetching nguyên trạng.
- [x] Reviewer độc lập kiểm timing, boundary, giới hạn và a11y; sinh SVG/HTML local để người dùng xem.
- [x] Cập nhật checkpoint/graph; giữ local chờ người dùng duyệt, chưa commit/push.

**Nguồn chuẩn:** https://www.w3.org/TR/css-animations-1/#animation-delay ; https://www.w3.org/TR/css-easing-1/#step-easing-functions ; https://www.w3.org/TR/SVG/conform.html#secure-animated-mode .

## Kết quả

RED 16 fail/15 pass → focused GREEN 31 pass; full 246 pytest + 11 Node pass. Reviewer độc lập không có finding cần sửa, focused 45 pass. Preview HTML/7 SVG: `../.task-tools/spotify-clock-preview-20261112/index.html` tính từ gốc repo. Graph cập nhật 527 nodes / 745 edges / 36 communities. Chưa browser QA; timeline tests mô phỏng CSS nên không khẳng định hình thực tế. Người dùng đã cho phép phát hành bản đồng hồ, sau đó dừng chờ hướng mới.
