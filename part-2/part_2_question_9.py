"""
(2 điểm) Nhập vào một chuỗi. Hãy đếm số ký tự chữ cái, chữ số, và ký tự đặc biệt trong chuỗi đó.
Gợi ý: dùng isalpha(), isdigit(), và isalnum().
"""
chuoi = input("Nhap chuoi: ")
so_chu_cai = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.isalpha():
        so_chu_cai += 1
    elif ky_tu.isdigit():
        so_chu_so += 1
    else:
        so_ky_tu_dac_biet += 1
print(f"So ky tu chu cai: {so_chu_cai}", f"So ky tu chu so: {so_chu_so}", f"So ky tu dac biet: {so_ky_tu_dac_biet}")