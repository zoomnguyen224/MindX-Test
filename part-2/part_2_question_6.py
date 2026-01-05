"""
(1 điểm) Viết chương trình nhập vào một số nguyên n, in ra tất cả các số chẵn từ 0 đến n.
"""
n = int(input("Nhap so nguyen n: "))
"""
Chay for loop tu 0 den n+1, moi lan tang 2
In ra gia tri i
"""
for i in range(0, n+1, 2):
    print(i)
