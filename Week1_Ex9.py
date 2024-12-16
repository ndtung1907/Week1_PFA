# 4. Viết hàm total nhận số nguyên N làm tham số, hàm trả về tống các chữ số của số N (chẳng hạn N = 132 thì hàm total trả về 6)
def total(n):
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    return sum
n = int(input("Nhập số nguyên N: "))
print(f"Tổng các chữ số của {n}: {total(n)}")