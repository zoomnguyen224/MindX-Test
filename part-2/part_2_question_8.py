"""
(1 điểm) Cho danh sách numbers = [1][2][3][4][5]. Hãy tính tổng bình phương các phần tử trong danh sách.
"""
numbers = [1, 2, 3, 4, 5]
tong = 0
for number in numbers:
    tong += (number * number)
print(tong)