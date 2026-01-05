"""
(1 điểm) Viết hàm is_prime(n) trả về True nếu n là số nguyên tố, ngược lại trả về False.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Nhap so nguyen n: "))
print(is_prime(n))
