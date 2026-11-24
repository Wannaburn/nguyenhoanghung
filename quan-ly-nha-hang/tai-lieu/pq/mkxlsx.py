from perm import ROLES,M,STORES
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.comments import Comment
F='Arial';thin=Side(style='thin',color='BFC7C2');B=Border(left=thin,right=thin,top=thin,bottom=thin)
H=PatternFill('solid',fgColor='1F6B4F');HF=Font(name=F,bold=True,color='FFFFFF');N=Font(name=F,size=10);BO=Font(name=F,bold=True,size=10)
Y=PatternFill('solid',fgColor='FFF2CC');G=PatternFill('solid',fgColor='E9EDE6')
def hdr(ws,row,vals,widths=None):
    for i,v in enumerate(vals,1):
        c=ws.cell(row,i,v);c.font=HF;c.fill=H;c.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True);c.border=B
    if widths:
        for i,w in enumerate(widths,1):ws.column_dimensions[chr(64+i)].width=w
def body(c,bold=False,center=False,fill=None):
    c.font=BO if bold else N;c.border=B;c.alignment=Alignment(vertical='center',wrap_text=True,horizontal='center' if center else 'left')
    if fill:c.fill=fill
def title(ws,t,sub):
    ws['A1']=t;ws['A1'].font=Font(name=F,bold=True,size=14,color='1F6B4F');ws['A2']=sub;ws['A2'].font=Font(name=F,italic=True,size=10,color='5D6A62')
wb=Workbook()
# 1. Hướng dẫn
ws=wb.active;ws.title='Hướng dẫn'
title(ws,'PHÂN QUYỀN XEM DỮ LIỆU – APP SỔ KẾ HOẠCH NHÀ HÀNG PAPAXỐT','Lưu hành nội bộ · Bộ phận xây dựng: Vận hành (AM3) · Đề nghị → AM → OM → BOD')
rows=[('Cách dùng file',''),
 ('1. Sheet "Chức vụ"','5 cấp: OM → AM → RGM → ARGM → Nhân viên, kèm phạm vi dữ liệu từng cấp.'),
 ('2. Sheet "Ma trận phân quyền"','Mỗi dòng là một dữ liệu/chức năng trong app, mỗi cột là một chức vụ. Chọn mức quyền trong ô (danh sách thả xuống).'),
 ('3. Sheet "Cửa hàng & zone"','Gán cửa hàng cho AM, ghi tên RGM/ARGM. Ô vàng là ô cần điền.'),
 ('4. Sheet "Người dùng"','Danh sách người được cấp quyền. Cột Phạm vi và Số quyền tự tính theo chức vụ.'),
 ('',''),
 ('Ký hiệu mức quyền',''),
 ('D – Duyệt','Xem, nhập/sửa và phê duyệt.'),
 ('S – Sửa','Xem và nhập/sửa.'),
 ('X – Xem','Chỉ xem, không sửa.'),
 ('— Không','Không thấy dữ liệu này.'),
 ('',''),
 ('Ô cần điền','Nền vàng.'),
 ('Lưu ý','Ma trận này đã được gắn sẵn vào app. Khi sửa ma trận, gửi lại file để cập nhật app cho khớp.'),
 ('Lưu ý bảo mật','App hiện lưu dữ liệu trên từng trình duyệt và chọn chức vụ khi mở app, chưa có đăng nhập. Phân quyền hiện chỉ giúp mỗi người thấy đúng phần việc của mình, chưa chặn được người cố ý đổi chức vụ. Muốn bảo mật thật cần làm đăng nhập + máy chủ dữ liệu.'),
]
for i,(a,b) in enumerate(rows,4):
    ws.cell(i,1,a).font=BO if (not b or a[:1].isdigit() is False) else N;ws.cell(i,2,b).font=N;ws.cell(i,2).alignment=Alignment(wrap_text=True,vertical='top')
    if a in('Cách dùng file','Ký hiệu mức quyền'):ws.cell(i,1).font=Font(name=F,bold=True,size=11,color='1F6B4F')
for a,col in [('D – Duyệt','1F6B4F'),('S – Sửa','6FB38F'),('X – Xem','DDE8F1'),('— Không','E5E7E6')]:
    r=[i for i,(x,_) in enumerate(rows,4) if x==a][0];ws.cell(r,1).fill=PatternFill('solid',fgColor=col);ws.cell(r,1).font=Font(name=F,bold=True,color='FFFFFF' if col=='1F6B4F' else '18221D')
r=[i for i,(x,_) in enumerate(rows,4) if x=='Ô cần điền'][0];ws.cell(r,1).fill=Y
ws.column_dimensions['A'].width=30;ws.column_dimensions['B'].width=95
# 2. Chức vụ
ws=wb.create_sheet('Chức vụ');title(ws,'CHỨC VỤ VÀ PHẠM VI DỮ LIỆU','Theo sơ đồ tổ chức: BOD → OM → AM → RGM → ARGM → NV')
hdr(ws,4,['Mã','Chức vụ','Cấp','Báo cáo cho','Phạm vi dữ liệu','Mô tả vai trò'],[9,28,9,14,34,70])
for i,r in enumerate(ROLES,5):
    for j,v in enumerate(r,1):body(ws.cell(i,j,v),bold=j==1,center=j in(1,3))
    ws.row_dimensions[i].height=34
# 3. Ma trận
ws=wb.create_sheet('Ma trận phân quyền');title(ws,'MA TRẬN PHÂN QUYỀN XEM DỮ LIỆU','D = Duyệt · S = Sửa · X = Xem · — = Không')
hdr(ws,4,['STT','Nhóm','Dữ liệu / chức năng','OM','AM','RGM','ARGM','NV','Ghi chú','Mã (dùng cho app)'],[6,20,46,8,8,8,8,8,52,14])
start=5
for i,(k,g,t,*lv,note) in enumerate(M):
    r=start+i;vals=[i+1,g,t,*lv,note,k]
    for j,v in enumerate(vals,1):body(ws.cell(r,j,v),center=j in(1,4,5,6,7,8),fill=G if j==2 else None)
    ws.cell(r,10).font=Font(name=F,size=9,color='8A968E')
end=start+len(M)-1
dv=DataValidation(type='list',formula1='"D,S,X,—"',allow_blank=False,showErrorMessage=True,errorTitle='Mức quyền',error='Chọn D, S, X hoặc —');ws.add_data_validation(dv);dv.add(f'D{start}:H{end}')
for val,fill,fc in [('"D"','1F6B4F','FFFFFF'),('"S"','6FB38F','0B1410'),('"X"','DDE8F1','2C5F8A'),('"—"','EEEEEE','8A968E')]:
    ws.conditional_formatting.add(f'D{start}:H{end}',CellIsRule(operator='equal',formula=[val],fill=PatternFill('solid',fgColor=fill),font=Font(name=F,bold=True,color=fc)))
s=end+2;ws.cell(s,3,'Tổng hợp số quyền theo chức vụ').font=Font(name=F,bold=True,color='1F6B4F')
for k,(lab,sym) in enumerate([('Số mục được Duyệt (D)','D'),('Số mục được Sửa (S)','S'),('Số mục chỉ Xem (X)','X'),('Số mục Không thấy (—)','—'),('Tổng số mục được thấy','*')]):
    r=s+1+k;body(ws.cell(r,3,lab),bold=sym=='*')
    for c in 'DEFGH':
        f=f'=COUNTA({c}{start}:{c}{end})-COUNTIF({c}{start}:{c}{end},"—")' if sym=='*' else f'=COUNTIF({c}{start}:{c}{end},"{sym}")'
        cell=ws[f'{c}{r}'];cell.value=f;body(cell,bold=sym=='*',center=True)
ws.freeze_panes='D5';ws.auto_filter.ref=f'A4:J{end}'
# 4. Cửa hàng & zone
ws=wb.create_sheet('Cửa hàng & zone');title(ws,'CỬA HÀNG VÀ ZONE QUẢN LÝ','Điền AM phụ trách, RGM, ARGM cho từng cửa hàng (ô vàng)')
hdr(ws,4,['Mã cửa hàng','Cửa hàng','AM phụ trách','RGM','ARGM 1','ARGM 2','Ghi chú'],[16,34,14,24,24,24,30])
for i,(code,name,am) in enumerate(STORES,5):
    vals=[code,name,am,'','','','Zone AM3 (theo sổ tay)' if am else '']
    for j,v in enumerate(vals,1):body(ws.cell(i,j,v),bold=j==1,fill=Y if j in(3,4,5,6) and not (j==3 and am) else None)
dva=DataValidation(type='list',formula1='"AM1,AM2,AM3"',allow_blank=True);ws.add_data_validation(dva);dva.add(f'C5:C{4+len(STORES)}')
ws.cell(5,3).comment=Comment('Zone AM3 lấy theo sổ tay quy trình PPX (DD, HH, NKKN, SVH, PCAC, NAT). Các cửa hàng còn lại cần điền AM phụ trách.','Claude')
# 5. Người dùng
ws=wb.create_sheet('Người dùng');title(ws,'DANH SÁCH NGƯỜI DÙNG ĐƯỢC CẤP QUYỀN','Dòng 5 là ví dụ. Điền từ dòng 6; cột F, G tự tính.')
hdr(ws,4,['STT','Họ tên','Chức vụ (mã)','Cửa hàng / zone','Ngày cấp quyền','Phạm vi dữ liệu (tự tính)','Số mục được thấy (tự tính)','Ghi chú'],[6,26,14,22,15,36,16,30])
n=len(STORES)
for r in range(5,45):
    ws.cell(r,1,r-4)
    for j in range(1,9):body(ws.cell(r,j),center=j in(1,3,5,7),fill=Y if j in(2,3,4,5) and r>5 else None)
    ws.cell(r,6).value=f'=IF(C{r}="","",IFERROR(INDEX(\'Chức vụ\'!$E$5:$E$9,MATCH(C{r},\'Chức vụ\'!$A$5:$A$9,0)),"Mã chức vụ chưa đúng"))'
    ws.cell(r,7).value=f'=IF(C{r}="","",IFERROR(INDEX(\'Ma trận phân quyền\'!$D${end+7}:$H${end+7},MATCH(C{r},\'Ma trận phân quyền\'!$D$4:$H$4,0)),""))'
    ws.cell(r,5).number_format='DD/MM/YYYY'
ws['B5']='Nguyễn Hoàng Hưng';ws['C5']='AM';ws['D5']='AM3 (DD, HH, NKKN, SVH, PCAC, NAT)';ws['H5']='Ví dụ – dữ liệu từ sổ tay PPX'
import datetime;ws['E5']=datetime.date(2026,11,22)
dvr=DataValidation(type='list',formula1='"OM,AM,RGM,ARGM,NV"',allow_blank=True);ws.add_data_validation(dvr);dvr.add('C5:C44')
dvs=DataValidation(type='list',formula1=f"='Cửa hàng & zone'!$A$5:$A${4+n}",allow_blank=True,showErrorMessage=False);ws.add_data_validation(dvs);dvs.add('D6:D44')
ws.freeze_panes='C5'
for w in wb.worksheets:w.sheet_view.showGridLines=False
wb.save('Phan-quyen-app-PPX.xlsx');print('saved',end)
