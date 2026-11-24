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
3. **Hôm nay** (`#tong-quan`), viết lại 24/11/2026 theo **17 hạng mục vận hành PPX** (10 ngày, 4 tuần, 3 tháng):
   - Nguồn: Drive "Đào tạo AM Hưng": `HM công việc.xlsx` (giờ, công cụ), `QĐ KHỐI NHÀ HÀNG/Bộ mở - đóng ca các vị trí & 6 note.xlsx`, `QĐ KHỐI NHÀ HÀNG/BỘ QUY ĐỊNH FULL 5S.xlsx`.
   - Dữ liệu trong app: `HM_DAY`, `HM_WEEK`, `HM_MONTH`, `OC` (bộ mở/đóng ca QL, PV, O2C, PC, KSM, BEP), `NOTE6` (47 chú ý), `SAFE` (note an toàn đỏ), `S5_STD`/`S5_AREA` (5 tiêu chuẩn sạch × 9 khu vực).
   - Lưu ở `S.ops['D<ngày>|<mã CH>']`, `W<năm>-<tuần>|CH`, `M<yyyy-mm>|CH`; khóa `hm<n>.<lượt>`, `oc.<nhóm>.<o|c>.<i>.<ca>`, `n6.<mục>.<i>.<ca>`, `sf.<nhóm>.<i>.<ca>`, `s5.<khu>.<chuẩn>` = ok/ng, `note.<n>`, `w<n>`, `m<n>`. Đã tách theo cửa hàng, dùng được cho trang Điều hành zone.
   - Bố cục: Cần chú ý (thêm: HM ngày quá giờ, note an toàn đỏ chưa xong trước 13h / 20h) → tổng 17 HM (chọn CH) → Note an toàn đỏ → 10 HM ngày theo giờ (mở rộng: HM1 bộ mở/đóng ca, HM9 6 note, HM10 5S, HM2 DSR) | cột phải: HM tuần/tháng, doanh thu, việc riêng, sắp tới → sổ giao ca.
   - NV chỉ thấy và tick bộ mở/đóng ca của bộ phận mình.
   - Checklist khung giờ cũ (`SHIFT_CL`, tổng hợp nhiều thương hiệu) đã bỏ khỏi app; file `tai-lieu/daily/` giữ làm tham khảo.
   - **Chờ anh Hưng xác nhận**: 3 mục note an toàn đỏ đánh dấu "chờ xác nhận" (sống–chín/sát sàn, bình chữa cháy/lối thoát hiểm, sàn bếp/dao chảo); giờ của HM 8–10 lấy theo khung "Tập trung vận hành" 10h30–14h & 17h–21h; HM tuần/tháng chưa có thứ/ngày hạn trong file nên chỉ tick trong tuần/tháng.
   - Script: `tai-lieu/hm17/patch_homnay.py` (đã chạy, chỉ để lưu vết).
4. **Cẩm nang** (cập nhật 25/11/2026): 4 tab mới ở đầu, vẽ theo skill `ve-hinh-15-mau`, mã nguồn ở `tai-lieu/camnang/hb_ppx.js` (đã chèn vào app bằng `patch_camnang.py`):
   - **Deadline công việc** (mẫu 15 timeline): dữ liệu `DL`, nhóm Quý → Tháng → Tuần → Ngày → Giờ, lọc theo nhóm, nút "Chỉ việc của AM", tô sáng mốc trùng hôm nay. Nguồn chính: `Deadline báo cáo công việc hệ thống.xlsx`.
   - **Kiến thức vận hành PPX** (mẫu 10 giải phẫu): mặt cắt nhà hàng 9 vị trí + thẻ A–E: 17 HM, 6 NOTE, Full 5S (9 tiêu chuẩn set up, bộ màu FOH/BOH), 5 tiêu chuẩn sạch, note an toàn đỏ.
   - **Quy định công ty** (mẫu 10 giải phẫu): nhân viên PPX với 6 bộ phận = 6 nhóm `QD` (thăng tiến – đào tạo; lương thưởng phúc lợi; nội quy tác phong; tiền & chi phí; hàng hóa; vận hành & sự vụ).
   - **Kiến thức ngành** (mẫu 02 lộ trình): Module 7–16 bộ Leading A Shift (`MOD`), đánh dấu đã học lưu `S.mod`. File Module 11 trên Drive trùng nội dung Module 7.
   - Đã bỏ 3 tab cũ (Bản đồ công việc, Lộ trình 90 ngày, Kiến thức & công thức) khỏi giao diện; code cũ (`HB`, `hbMap`, `hbPath`, `hbKb`) còn trong file nhưng không hiển thị.
   - Giao diện kiểu code (`patch_code_style.py`): góc vuông, font JetBrains Mono, thanh cửa sổ terminal kèm tên file (deadline.ts, van-hanh.svg, quy-dinh.md, nganh.roadmap), nền lưới, 4 ô chỉ số dạng biến (deadline.homNay, vanHanh.hangMuc, quyDinh.nhom, module.daHoc).
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
