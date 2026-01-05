"""
(2 điểm) Viết chương trình quản lý sinh viên đơn giản:
Cho phép nhập danh sách sinh viên (tên, điểm).
In ra tên sinh viên có điểm cao nhất.
Tính điểm trung bình của cả lớp.
"""
danh_sach_sinh_vien = []
diem_cao_nhat = 0
sinh_vien_cao_nhat = ""
diem_trung_binh = 0
while True:
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    danh_sach_sinh_vien.append((ten, diem))
    #Cap nhat diem cao nhat
    if diem > diem_cao_nhat:
        diem_cao_nhat = diem
        sinh_vien_cao_nhat = ten
    #Cap nhat diem trung binh
    diem_trung_binh += diem
    if input("Nhap them sinh vien (y/n): ") == "n":
        break

print(danh_sach_sinh_vien)
print(f"Ten sinh vien co diem cao nhat: {sinh_vien_cao_nhat}","-",f"Diem: {diem_cao_nhat}")
print(f"Diem trung binh cua ca lop: {diem_trung_binh / len(danh_sach_sinh_vien)}")
