from flask import Flask, request, render_template

app = Flask(__name__)

mon_hoc = {
    'toan': 'Toán',
    'van': 'Văn',
    'anh': 'Tiếng Anh',
    'khoahoc': 'Khoa học',
    'lichsu_diali': 'Lịch sử - Địa Lí',
    'congnghe': 'Công Nghệ',
    'tinhoc': 'Tin Học',
    'avbn': 'AVBN',
    'gdcd': 'GDCD'
}

def tinh_trung_binh(diem_list, he_so_list):
    tong = 0
    tong_he_so = 0
    for d, h in zip(diem_list, he_so_list):
        diem = float(d)
        he_so = int(h)
        tong += diem * he_so
        tong_he_so += he_so
    return round(tong / tong_he_so, 2) if tong_he_so > 0 else 0

@app.route('/')
def index():
    return render_template('index.html', subjects=mon_hoc)

@app.route('/result', methods=['POST'])
def result():
    ket_qua = {}
    tong_tb = 0

    for key, name in mon_hoc.items():
        diem_list = request.form.getlist(f'{key}_score[]')
        he_so_list = request.form.getlist(f'{key}_weight[]')
        if diem_list:
            tb_mon = tinh_trung_binh(diem_list, he_so_list)
            ket_qua[name] = tb_mon
            tong_tb += tb_mon

    tb_chung = round(tong_tb / len(ket_qua), 2) if ket_qua else 0

    html_kq = "<div class='container mt-5'><h2>Kết quả điểm trung bình:</h2><ul class='list-group'>"
    for mon, tb in ket_qua.items():
        html_kq += f"<li class='list-group-item'>{mon}: <strong>{tb}</strong></li>"
    html_kq += f"</ul><h3 class='mt-3'>👉 Trung bình tất cả các môn: <b>{tb_chung}</b></h3>"
    html_kq += "<a class='btn btn-primary mt-3' href='/'>⏪ Quay lại</a></div>"
    return html_kq

if __name__ == '__main__':
    app.run(debug=True)
