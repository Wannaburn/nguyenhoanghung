# Đọc 2 file xuất từ Odoo (papaxot.hyperdata.vn → Báo cáo tổng quan → "Doanh thu theo ngày, ca, kênh")
# và ghi dữ liệu vào hằng ODOO_SALES trong quan-ly-nha-hang/index.html.
# Cách dùng: python3 -I import_sales.py <Sales-...-theo-cua-hang-ngay.xlsx> <Pivot_Doanh_thu_...xlsx> <file html đích>
# LƯU Ý: repo GitHub đang công khai. Chỉ ghi số liệu vào BẢN SAO index.html dùng để publish Artifact riêng tư, KHÔNG commit bản có số liệu.
import sys, json, re, pathlib, datetime, openpyxl

STORE = {'Papaxot Đồng Đen': '003_PPX-DD', 'Papaxot Hoa Hồng': 'HH', 'Papaxot Nam Kỳ Khởi Nghĩa': '010_PPX-NKKN',
         'Papaxot Phượng Các': 'Café-PCAC', 'Papaxot Sư Vạn Hạnh': '008_PPX-SVH', 'Papaxot Nguyễn Ảnh Thủ': 'NAT'}

def daily(path):
    ws = openpyxl.load_workbook(path, data_only=True)['Chi tiết ngày-cửa hàng']
    out = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        if not r[0] or r[1] not in STORE: continue
        d = r[0].date().isoformat() if isinstance(r[0], datetime.datetime) else str(r[0])[:10]
        out.setdefault(STORE[r[1]], {})[d] = [int(r[2] or 0), int(r[3] or 0), int(r[4] or 0), int(r[5] or 0)]  # gộp, CK, thuần, bill
    return out

def channels(path):
    rows = list(openpyxl.load_workbook(path, data_only=True).worksheets[0].iter_rows(values_only=True))
    head = rows[3]; names = []
    for i, v in enumerate(head):
        if v and i > 0: names.append((v.strip(), i))
    names = [(n, i) for n, i in names if i + 4 < len(head)]
    ch = {}
    for r in rows[5:]:
        lab = (r[0] or '').strip()
        if lab not in STORE: continue
        st = ch.setdefault(STORE[lab], {})
        for n, i in names:
            net, bills = r[i + 2], r[i + 3]
            if net or bills:
                a = st.setdefault(n, [0, 0]); a[0] += int(net or 0); a[1] += int(bills or 0)
    return ch, [n for n, _ in names]

def main(f1, f2, out):
    d = daily(f1); ch, chn = channels(f2)
    days = sorted({k for s in d.values() for k in s})
    data = {'src': 'Odoo papaxot.hyperdata.vn · Báo cáo tổng quan · Doanh thu theo ngày, ca, kênh', 'from': days[0], 'to': days[-1],
            'updated': datetime.date.today().isoformat(), 'channels': chn, 'daily': d, 'ch': ch}
    # kiểm tra tổng
    tot = sum(v[2] for s in d.values() for v in s.values()); bills = sum(v[3] for s in d.values() for v in s.values())
    print('Doanh thu thuần', tot, 'bill', bills, 'từ', days[0], 'đến', days[-1])
    for code, s in d.items(): print(code, sum(v[2] for v in s.values()), 'kênh', sum(v[0] for v in ch.get(code, {}).values()))
    p = pathlib.Path(out); s = p.read_text(encoding='utf-8')
    js = 'const ODOO_SALES=' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';'
    s, n = re.subn(r'const ODOO_SALES=(?:\{.*?\}|null);[^\n]*', lambda m: js, s, count=1, flags=re.S)
    if n == 0:
        marker = '/* ---------- Doanh thu & mục tiêu ---------- */'
        assert s.count(marker) == 1
        s = s.replace(marker, '/* Dữ liệu bán hàng thật từ Odoo (tạo bởi tai-lieu/odoo/import_sales.py) */\n' + js + '\n' + marker)
    p.write_text(s, encoding='utf-8'); print('Đã ghi ODOO_SALES vào', p)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
