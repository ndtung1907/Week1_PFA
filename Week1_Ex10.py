# 5. Viết hàm is Fibo nhận số nguyên N làm tham số, hàm kiểm tra xem N có phải số fibonacci hay không? Trả về True nếu đúng, ngược lại trả về False
def is_fibo(n):
    if n < 2:
        return True
    a , b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n: return True
    return False
n = int(input("Nhập số nguyên N: "))
print(f"{n} là số fibonacci" if is_fibo(n) else f"{n} không phải số fibonacci")
