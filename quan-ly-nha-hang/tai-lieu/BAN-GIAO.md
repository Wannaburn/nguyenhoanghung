# Bàn giao dự án: Sổ Kế Hoạch Nhà Hàng (PPX)

Cập nhật: 24/11/2026. Người dùng: anh Hưng, Area Manager 3 (AM3) Papaxốt, zone DD, HH, NKKN, SVH, PCAC, NAT. Giao tiếp bằng tiếng Việt.

## Vị trí

- Nhánh git: `claude/restaurant-management-app-4ga6e3`. PR #1 vào `main` (chưa merge).
- App: `quan-ly-nha-hang/index.html`, một file HTML duy nhất, JS thuần, dữ liệu lưu `localStorage` (key `so-ke-hoach-nha-hang.v1`).
- Bản xem thử (Artifact): https://claude.ai/artifact/44F3LHSucyp564n3eS4K8a
  - Trước khi cập nhật Artifact, phải đọc nó bằng `action: "read"` rồi mới publish với `url`.
  - Nội dung publish lên Artifact = `index.html` bỏ 6 dòng đầu (doctype, html, head, meta) và dòng `</html>` cuối. Artifact tự bọc skeleton.
- Sau khi merge, app chạy tại `https://wannaburn.github.io/nguyenhoanghung/quan-ly-nha-hang/`.
- `tai-lieu/`: script và file Excel nguồn (xem cuối file).

## Các màn hình đã có

1. **Chọn chức vụ** khi vào app lần đầu: OM, AM (chọn zone AM1–3), RGM, ARGM (chọn cửa hàng), NV (chọn tên mình). Phân quyền theo ma trận trong `PERM` (D Duyệt / S Sửa / X Xem / — Không). `can(key,min)`, `guard()`, `applyLocks()` ẩn nút và form không có quyền. Chưa có đăng nhập, phân quyền chỉ để mỗi người thấy đúng phần việc, chưa phải bảo mật.
2. **Bản đồ nhà hàng** (màn hình mặc định, `#nha-hang`): bản đồ pixel kiểu nông trại, 4 khu đất cho 5 cửa hàng (NKKN + PCAC chung sân vườn, HH, DD, SVH). Cửa sổ sáng khi tầng có người, ống khói khi bếp có người, bong bóng đếm người và cảnh báo chưa vào ca. Bấm vào thì mở **mặt cắt theo tầng**. Cấu hình trong `SITES`:
   - NKKN + PCAC: bếp chung | sân vườn | bar chung.
   - HH: Lầu 3, 2, 1 khu khách; Trệt quầy + bếp (*giả định*); Hầm quán cà phê.
   - DD: Lầu 2, Lửng khu khách; Trệt khu khách + bếp (bếp *giả định*).
   - SVH: Lầu 1, Trệt (*giả định hoàn toàn*).
   - Chờ anh Hưng xác nhận các phần giả định và việc có thêm NAT hay không.
   Thanh thời gian, tua cả ngày, chấm công vào/ra ca, lịch ca dạng Gantt, nhân viên có `store` và `zone` (floorId:partIndex).
3. **Hôm nay** (`#tong-quan`, đã đổi từ Tổng quan để bỏ trùng với Doanh thu):
   - Cần chú ý: chưa vào ca, chưa nhập DSR (quá 10h là đỏ), DT hôm qua < 90%, checklist quá giờ, giao ca chưa đọc, nhắc việc, ngày lễ.
   - Doanh thu một dòng.
   - Checklist ca theo khung giờ `SHIFT_CL` (QL, PV, TN, BEP, BAR), tick lưu ở `S.chk['D'+ngày]`.
   - Sổ giao ca `S.logbook` (Doanh thu, Nhân sự, Hàng hóa, Vấn đề tồn đọng, đã đọc).
4. **Cẩm nang**: 47 công việc / 7 nhóm / 5 tần suất, lộ trình 90 ngày, kiến thức + máy tính nhanh. Nội dung do Claude tự viết theo kiến thức chung, chưa theo chuẩn PPX. Đã liệt kê các chỗ lệch (tủ mát 1–8°C, kiểm nhiệt 3 lần/ngày, BLAST, tốc độ ra món, kiểm hàng nhập ≤3h). Đã đề xuất viết lại theo sổ tay PPX, chưa làm.
5. **Kế hoạch** Năm → Quý → Tháng → Tuần → Ngày, mục tiêu doanh thu tự chia xuống.
6. **Doanh thu** (chung một quán, chưa tách theo cửa hàng), **Lịch** (âm lịch Hồ Ngọc Đức, ngày lễ VN, nhắc việc lặp), **Lưu ý tháng**, **Cài đặt** (bảng quyền, đổi chức vụ, sao lưu).

## Việc tiếp theo đã đề xuất (chờ anh Hưng duyệt)

- **Bước 3**: tách doanh thu theo cửa hàng (`S.revenue` hiện là theo ngày, chung), rồi làm trang **"Điều hành zone"** cho OM/AM: bảng so sánh các cửa hàng (DSR trước 10h, % checklist, chưa vào ca, DT hôm qua) với đèn xanh/vàng/đỏ.
- Viết lại Cẩm nang theo chuẩn PPX.
- Xác nhận cấu hình tầng HH, DD, SVH, NAT.
- Về lâu dài: đăng nhập + máy chủ dữ liệu chung để nhân viên tự chấm công trên điện thoại.

## Cách làm việc đã dùng

- Sửa app bằng script Python thay chuỗi có `assert count==1`. Kiểm tra `node --check` phần `<script>`. Chạy thử bằng Playwright ở 1300px và 400px (dùng `page.clock.install` để cố định giờ), xem lỗi JS và tràn ngang.
- Mỗi thay đổi: commit (tiếng Việt) → push nhánh → publish lại Artifact.
- Ma trận phân quyền có một nguồn duy nhất `tai-lieu/pq/perm.py`. Sửa xong chạy `python3 mkxlsx.py` (trong `pq/`) để tạo Excel, và `python3 pq/mkjs.py` (trong `tai-lieu/`) để tạo `pq/perm.js`, rồi thay các dòng `const PERM=`, `PERM_ROWS`, `ROLE_INFO`, `STORE_LIST` trong app.
- Checklist khung giờ có nguồn `tai-lieu/daily/mk.py` (tạo Excel; dữ liệu QL/PV/TN/BEP/BAR cũng là `SHIFT_CL` trong app). Tổng hợp từ Drive của anh Hưng: PPX "Checklist bộ phận theo khung giờ", Ăn Được Phúc "Checklist Management" + "Chi tiết công việc", Phúc Lộc Thọ "TnD-SOP-FOH" + "Handover-Sealing book", Highlands "Shift Leader Skills", Phúc Long "Sổ tay vận hành" + "Lobby".
- Thông tin nội bộ PPX (cơ cấu, mã cửa hàng, deadline, câu thoại) nằm trong skill `anthropic-skills:viet-quy-trinh-ppx`.
