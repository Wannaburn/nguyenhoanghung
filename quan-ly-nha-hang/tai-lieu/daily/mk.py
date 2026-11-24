from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.worksheet.datavalidation import DataValidation
F='Arial';th=Side(style='thin',color='BFC7C2');B=Border(left=th,right=th,top=th,bottom=th)
G='1F6B4F';HF=Font(name=F,bold=True,color='FFFFFF',size=10);N=Font(name=F,size=10);BO=Font(name=F,bold=True,size=10)
PH={'MỞ CA':'E3F1E8','GIỮA CA':'FFF6DB','GIAO CA':'E2ECF5','CA TỐI':'F3E6F3','CUỐI CA':'F6E0DB'}
SRC={'PPX':'PPX – Checklist bộ phận theo khung giờ','ADP':'Ăn Được Phúc – Manager/Daily Checklist, Chi tiết công việc','PLT':'Phúc Lộc Thọ – SOP FOH 12/2020, Sổ bàn giao tiền','HL':'Highlands – Shift Leader Skills','PL':'Phúc Long – Sổ tay vận hành, Lobby'}
# (giai đoạn, khung giờ, nhóm, chi tiết, nguồn)
QL=[
('MỞ CA','8h00 – 9h00','Kiểm tra bên ngoài','Vỉa hè, bãi xe, bảng hiệu, đèn, cửa kính, cây cảnh: sạch, sáng, an toàn','ADP'),
('MỞ CA','8h00 – 9h00','Kiểm tra đóng ca hôm trước','Thiết bị, đèn, quạt hút, máy lạnh, gas; vệ sinh đóng ca của từng bộ phận','ADP, PPX'),
('MỞ CA','8h00 – 9h00','Tiền & sổ bàn giao','Kiểm doanh thu ca trước, tiền vốn, quỹ vận hành, niêm phong; ký sổ bàn giao tiền quản lý','ADP, PLT'),
('MỞ CA','8h00 – 9h00','Đọc logbook','Đọc logbook / sổ bàn giao ca, mail; ghi việc tồn đọng cần xử lý trong ngày','ADP, PPX'),
('MỞ CA','8h00 – 9h00','Hàng hóa & chất lượng','Kiểm tra xả hàng bếp, quầy ra món, bar; nhiệt độ tủ; thử cảm quan món, xốt','PPX, ADP'),
('MỞ CA','8h00 – 9h00','Quầy thu ngân','Kiểm tài sản quầy; giao tiền vốn cho thu ngân; giá và CTKM trên POS/app đúng memo, mở món đã khóa','PPX, PLT'),
('MỞ CA','8h00 – 9h00','Phân công','Kiểm tra bảng phân công 5 nhóm (Phục vụ – Thu ngân – Bar – KSM – Bếp); sổ đặt bàn hôm nay','PPX, ADP'),
('MỞ CA','8h00 – 9h00','Daily checklist','Đi một vòng kiểm tra tổng thể trước giờ đón khách: sảnh, toilet, bar, bếp, KV ra món. Đánh V/X, lỗi phải sửa ngay trong ca','ADP'),
('MỞ CA','9h00 – 9h30','Briefing đầu ca','Đồng phục, tác phong, sức khỏe NV; plan sale, TC, target thu ngân; món cần upsale; phân vị trí; CTKM; nhắc lại lỗi cũ','PPX, ADP, HL'),
('MỞ CA','9h30 – 10h30','Công việc quản lý','Chuẩn bị hàng trả; nhận và kiểm hàng nhập (cân, HSD, nhiệt độ)','PPX'),
('MỞ CA','9h30 – 10h30','Công việc quản lý','Hoàn tất đặt hàng BTT trước 10h; gửi DSR, tồn trước 10h; trả lời mail, báo cáo','PPX'),
('GIỮA CA','10h30 – 14h30','Tập trung vận hành','Thường trực ở sảnh; kiểm soát thao tác NV, chất lượng món, quy trình; hỗ trợ và hỏi ý kiến khách; kiểm soát đơn delivery','PPX, ADP'),
('GIỮA CA','10h30 – 14h30','Kiểm tra 9 note','Kiểm tra 9 note theo khung giờ quy định, 30 phút/lần','PPX'),
('GIỮA CA','10h30 – 14h30','Phối hợp bộ phận','Di chuyển giữa các bộ phận, gỡ điểm tắc; dọn bàn trong tối đa 10 phút sau khi khách về','ADP, PL'),
('GIAO CA','14h00 – 15h00','Giao ca nhân viên','Kiểm tra xả hàng, chất lượng giao ca từng bộ phận; thu ngân kiểm đếm tiền, voucher, ký sổ bàn giao','PPX, ADP, PLT'),
('GIAO CA','14h00 – 15h00','Chuẩn bị ca tối','Cập nhật hàng hóa còn/thiếu, bổ sung CCDC cho ca tối; kiểm tra đơn hàng NCC','ADP'),
('GIAO CA','15h00 – 16h00','Bàn giao ca quản lý','Bàn giao: doanh thu – nhân sự – hàng hóa – vấn đề tồn đọng ca sáng (ghi logbook)','PPX, ADP'),
('CA TỐI','16h00 – 17h30','Kiểm tra ca chiều','Xả hàng, chất lượng sản phẩm, tài sản quầy thu ngân, bảng phân công; bật bảng hiệu, đèn ngoài','PPX, ADP'),
('CA TỐI','16h00 – 17h30','Doanh thu ca sáng','Cập nhật doanh thu ca sáng, so với kế hoạch; đặt mục tiêu ca tối','ADP'),
('CA TỐI','17h30 – 18h00','Briefing ca tối','Đồng phục; plan sale, TC; món upsale; phân vị trí; CTKM; việc cần hoàn thành trong ca','PPX, ADP'),
('CA TỐI','18h00 – 21h00','Tập trung vận hành','Thường trực sảnh, kiểm soát chất lượng và quy trình, hỗ trợ khách; kiểm tra 9 note 30 phút/lần','PPX'),
('CUỐI CA','21h00 – 22h30','Hàng hóa','Đặt hàng ca tối / bổ sung (16–22h, AM duyệt); kiểm hàng sơ bộ; tổ chức NV đếm tồn vào sổ; xả hàng cho ngày mai','PPX, ADP'),
('CUỐI CA','21h00 – 22h30','Vệ sinh cuối ngày','Kiểm tra vệ sinh và chất lượng kết ca của từng bộ phận','PPX, ADP'),
('CUỐI CA','21h00 – 22h30','Doanh thu','Kết ca thu ngân cùng QL: in báo cáo, đếm tiền, voucher; hoàn tất DSR, số tồn cuối ngày; ghi sổ bàn giao tiền, niêm phong','PPX, PLT'),
('CUỐI CA','21h00 – 22h30','Logbook','Ghi vấn đề tồn đọng vào logbook; việc chưa xong đưa vào ưu tiên của ngày mai','ADP, HL'),
('CUỐI CA','22h30','Đóng cửa','Tắt điện, nước, gas, thiết bị không dùng; kiểm nhiệt độ tủ; quay clip giao ca; bàn giao bảo vệ (ký sổ), khóa cửa','PPX, ADP'),
]
PV=[
('MỞ CA','10h00 – 10h30','Tác phong','Vào ca, chấm công; đồng phục đúng chuẩn; cất điện thoại vào hộp quy định','ADP, PL'),
('MỞ CA','10h00 – 10h30','Kiểm tra thiết bị sảnh','Quạt, máy bắt côn trùng, đèn, wifi, tivi, máy lạnh','PPX'),
('MỞ CA','10h00 – 10h30','Vệ sinh','Quét nhà, hành lang; nhặt lá, cây cối; bàn ghế, tủ station, vách, tranh; toilet','PPX, PL'),
('MỞ CA','10h30 – 11h00','Chuẩn bị đón khách','Lau muỗng nĩa, đũa, kéo, kẹp; khay dụng cụ; vệ sinh menu; set up bàn theo chuẩn; chuẩn bị xốt, tablet ở station','PPX, ADP'),
('GIỮA CA','11h00 – 14h00','Phục vụ','Chào – tư vấn – order – phục vụ món – take care – thanh toán; dọn bàn tối đa 10 phút sau khi khách về','PPX, PL'),
('GIỮA CA','11h00 – 14h00','Duy trì','Thường xuyên kiểm tra vệ sinh khu vực; hỗ trợ thu ngân khi khách xếp hàng đông','ADP, PL'),
('GIAO CA','14h00 – 17h00','Vệ sinh giao ca','Quét nhà, bàn ghế, station; vệ sinh CCDC cho ca sau; làm vệ sinh theo lịch phân công; bàn giao ca tối','PPX, ADP'),
('CA TỐI','17h00 – 18h00','Chuẩn bị đón khách','Như mở ca: CCDC, khay, menu, set up bàn','PPX'),
('CA TỐI','18h00 – 21h30','Phục vụ','Phục vụ theo quy trình; take care khách; dọn bàn và set up bàn mới','PPX'),
('CUỐI CA','21h30 – 22h30','Vệ sinh cuối ngày','Khu vực ngưng phục vụ; CCDC; bàn ghế và phủ kín; giặt phơi khăn; lịch vệ sinh ngày/tuần','PPX'),
('CUỐI CA','22h30','Kiểm tra cuối ca','Tắt thiết bị sảnh; báo cáo công việc với QL ca trước khi về','PPX, ADP'),
]
TN=[
('MỞ CA','10h00 – 10h30','Tiền','Kiểm tiền két, doanh thu, lưu ý bàn giao ca tối hôm qua; nhận tiền vốn từ QL, kiểm tiền lẻ, ký sổ bàn giao','PPX, ADP, PLT'),
('MỞ CA','10h00 – 10h30','Thiết bị','Khởi động POS, máy in bill, giấy in, máy tool/payoo, tablet order, điện thoại bàn; đăng nhập phần mềm bằng ID của mình','PPX, ADP, PLT'),
('MỞ CA','10h00 – 10h30','Giá & CTKM','Mở món đã khóa trên app; giá và CTKM đúng memo; cập nhật CKTM trong ngày; kiểm tra mã QR thanh toán','PLT, ADP'),
('MỞ CA','10h30 – 11h00','Chuẩn bị đón khách','Tiền lẻ, giấy tờ, hóa đơn; thông tin đặt bàn (số bàn, số khách, CKTM); hỗ trợ bộ phận khác set up','PPX, ADP'),
('GIỮA CA','11h00 – 14h00','Thanh toán','Thanh toán nhanh, chính xác; bill và hóa đơn VAT đầy đủ; bill hủy phải có chữ ký NV và QL, ghi lý do','PPX, ADP, PLT'),
('GIAO CA','14h00 – 15h00','Kết ca sáng','In báo cáo kết ca; đếm tiền mặt, voucher cùng QL; bàn giao doanh thu; bàn giao tiền thối, bill chưa thanh toán, máy tool cho ca chiều; ký sổ','PPX, ADP, PLT'),
('CA TỐI','15h00 – 17h00','Nhận ca chiều','Nhận bàn giao tiền, voucher từ QL; kiểm tra lại thiết bị, set up quầy','PLT, ADP'),
('CUỐI CA','22h00 – 22h30','Kết ca','Kết ca, đếm két, bàn giao doanh thu cho QL; bàn giao thông tin cho ca sáng mai; tắt và sạc thiết bị; vệ sinh quầy','PPX, ADP'),
]
BEP=[
('MỞ CA','8h00 – 8h30','Thiết bị','Kiểm vệ sinh ca tối hôm trước; bật và kiểm tra gas, bếp, lò, lò chiên (dầu, nhiệt độ), nồi cơm, đèn, van nước; nhiệt độ tủ đông/mát','PPX, ADP'),
('MỞ CA','8h00 – 8h30','Hàng hóa','Kiểm số lượng tồn, chất lượng, HSD: thịt, rau, xốt, hàng khô; xả hàng đông lạnh nếu cần; chỉnh ngày nhãn','PPX'),
('MỞ CA','8h30 – 10h30','Chuẩn bị NL bán','Nấu cơm, nướng gà, chiên trứng, canh súp, luộc rau mì/rau cơm, sơ chế rau, pha bột, chia kim chi; ưu tiên NL đã hết','PPX'),
('MỞ CA','10h30 – 11h00','Chuẩn bị NL bán','Ép cơm, định hình gà chiên; nhận hàng nhập (kiểm trong 3 giờ)','PPX'),
('GIỮA CA','11h00 – 14h00','Làm món','Làm món đúng định lượng, thời gian; duy trì vệ sinh khu vực (Clean as you go)','PPX'),
('GIAO CA','14h00 – 15h00','Vệ sinh ca sáng','Rửa rau, cấp đá bảo quản; bọc NL dở dang; vệ sinh thiết bị, dụng cụ, kệ inox, sàn, cống; đổ rác; bàn giao ca','PPX'),
('CA TỐI','15h00 – 17h30','Chuẩn bị ca tối','Kiểm hàng hóa; chuẩn bị NL bán; ép cơm, định hình gà','PPX'),
('CUỐI CA','21h00 – 22h30','Kết ca','Kiểm đếm tồn; cấp đông lại hàng cần thiết; xả hàng ngày mai; hủy hàng (nếu có, ghi phiếu); vệ sinh toàn bộ; úp chảo, giặt khăn','PPX'),
('CUỐI CA','22h30','Đóng bếp','Kiểm nhiệt độ tủ đông/mát; tắt thiết bị và gas không dùng','PPX'),
]
BAR=[
('MỞ CA','8h00 – 8h30','Thiết bị','Tủ lạnh, máy Pepsi, bình CO2, máy ép ly, ấm đun; tủ mát giữ đúng nhiệt độ','PPX, PL'),
('MỞ CA','8h00 – 9h00','Chuẩn bị','HSD, chất lượng NVL tồn (syrup, trà, nước pha sẵn, decor); set up ly, ống hút, túi, ca đong; refill NVL, báo hàng hết/gần hết','PPX'),
('GIỮA CA','9h00 – 14h00','Pha chế','Pha theo bill, đúng định lượng; giao nước đúng bill/thẻ rung; kiểm nhập hàng','PPX'),
('GIAO CA','14h00 – 15h00','Vệ sinh & bàn giao','Vệ sinh thiết bị, kệ, bồn rửa, cống; đổ rác; pha nước giao ca; kiểm tồn; bàn giao chất lượng, HSD, vấn đề phát sinh','PPX'),
('CUỐI CA','21h00 – 22h30','Kết ca','Kiểm tồn; pha nước giao ca; vệ sinh chai syrup, CCDC, thiết bị, khu vực; chà sàn','PPX'),
('CUỐI CA','22h30','Kiểm tra','Nhiệt độ tủ mát; tắt thiết bị không dùng','PPX'),
]
def sheet(wb,title,rows,first=False,who='QL ca'):
    ws=wb.active if first else wb.create_sheet(title);ws.title=title
    ws['A1']=f'CHECKLIST CÔNG VIỆC HẰNG NGÀY – {title.upper()}';ws['A1'].font=Font(name=F,bold=True,size=14,color=G)
    ws['A2']='Cửa hàng: ____________     Ngày: ___/___/______     Lưu hành nội bộ · Bộ phận xây dựng: Vận hành · Bộ phận sử dụng: RGM/ARGM & NV';ws['A2'].font=Font(name=F,size=9,color='5D6A62')
    hd=['GIAI ĐOẠN','KHUNG GIỜ','NHÓM CÔNG VIỆC','CHI TIẾT','PHỤ TRÁCH','CHECK','GHI CHÚ','THAM KHẢO TỪ']
    for i,h in enumerate(hd,1):
        c=ws.cell(4,i,h);c.font=HF;c.fill=PatternFill('solid',fgColor=G);c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True);c.border=B
    for w,col in zip([11,14,22,64,12,8,20,18],'ABCDEFGH'):ws.column_dimensions[col].width=w
    r=5
    for ph,t,g,d,src in rows:
        vals=[ph,t,g,d,'','','',src]
        for i,v in enumerate(vals,1):
            c=ws.cell(r,i,v);c.border=B;c.font=BO if i in(1,3) else N;c.alignment=Alignment(vertical='center',wrap_text=True,horizontal='center' if i in(1,2,5,6) else 'left')
            if i<=2:c.fill=PatternFill('solid',fgColor=PH[ph])
        ws.cell(r,8).font=Font(name=F,size=9,color='5D6A62')
        r+=1
    dv=DataValidation(type='list',formula1='"✓,X"',allow_blank=True);ws.add_data_validation(dv);dv.add(f'F5:F{r-1}')
    ws.cell(r+1,1,'Đánh ✓ khi hoàn thành, X khi chưa làm và ghi lý do ở cột Ghi chú. Việc chưa đạt phải khắc phục ngay trong ca.').font=Font(name=F,italic=True,size=9)
    ws.cell(r+3,2,f'{who} sáng (ký, ghi rõ họ tên)').font=BO;ws.cell(r+3,4,f'{who} tối (ký, ghi rõ họ tên)').font=BO;ws.cell(r+3,7,'Người kiểm tra').font=BO
    ws.freeze_panes='A5';ws.sheet_view.showGridLines=False
    ws.page_setup.orientation='landscape';ws.page_setup.fitToWidth=1;ws.page_setup.fitToHeight=0;ws.sheet_properties.pageSetUpPr.fitToPage=True;ws.print_title_rows='4:4'
    return ws
wb=Workbook()
sheet(wb,'Quản lý',QL,True,'QL ca');sheet(wb,'Phục vụ',PV);sheet(wb,'Thu ngân',TN);sheet(wb,'Bếp',BEP);sheet(wb,'Pha chế',BAR)
ws=wb.create_sheet('Nguồn tham khảo');ws['A1']='TÀI LIỆU ĐÃ ĐỌC TỪ GOOGLE DRIVE';ws['A1'].font=Font(name=F,bold=True,size=14,color=G)
rows=[('Mã','Thương hiệu','Tài liệu','Đã lấy gì'),
('PPX','Papaxốt','Checklist bộ phận theo khung giờ.xlsx','Khung giờ 8h–22h30, công việc QL và 5 nhóm (Phục vụ, Thu ngân, Bar, KSM, Bếp), 9 note 30 phút/lần, briefing'),
('ADP','Ăn Được Phúc','Checklist Management.xlsx (Manager + Daily Checklist); Chi tiết công việc.xlsx','Kiểm tra bên ngoài, logbook, thử cảm quan món, Daily checklist trước giờ đón khách, cập nhật DT ca sáng cho ca tối, bàn giao bảo vệ'),
('PLT','Phúc Lộc Thọ','TnD-SOP-FOH (12/2020); PLT Handover-Sealing book; Memo SOP PLT-T&D-008','Mở ca bộ phận bán hàng (đăng nhập ID, mở món khóa trên app, CTKM đúng memo), quy định bill hủy, sổ bàn giao tiền vốn – quỹ – doanh thu – niêm phong'),
('HL','Highlands','Shift Leader Skills 1.pdf','Lên kế hoạch ngày 5 bước; việc chưa xong chuyển thành ưu tiên ngày hôm sau; briefing hằng ngày'),
('PL','Phúc Long','Sổ tay vận hành.pdf; 3. Lobby.pdf','Điện thoại cất hộp riêng, chấm vân tay vào/ra ca, dọn bàn tối đa 10 phút, hỗ trợ thu ngân khi đông, tủ mát 4–7°C'),
('','','',''),
('Lưu ý','','','Sổ tay Phúc Long là bản scan, chỉ đọc được một phần. Ăn Được Phúc là mô hình lẩu buffet nên các mục quầy buffet line đã bỏ hoặc chuyển thành kiểm tra quầy ra món. Khung giờ theo PPX; cửa hàng khác giờ mở cửa thì chỉnh lại cột Khung giờ.')]
for i,row in enumerate(rows,3):
    for j,v in enumerate(row,1):
        c=ws.cell(i,j,v);c.border=B if row[0] else Border();c.alignment=Alignment(wrap_text=True,vertical='top');c.font=HF if i==3 else (BO if j<=2 else N)
        if i==3:c.fill=PatternFill('solid',fgColor=G)
for w,col in zip([8,16,44,80],'ABCD'):ws.column_dimensions[col].width=w
ws.sheet_view.showGridLines=False
wb.save('Checklist-cong-viec-hang-ngay.xlsx');print(len(QL),len(PV),len(TN),len(BEP),len(BAR))
