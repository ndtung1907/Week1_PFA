# 5. Nhập số nguyên X, hãy đếm xem X có bao nhiêu chữ số, in ra chữ số đầu tiên của X
import math as m
x = int(input("Nhập số nguyên X: "))
count = 0
first_num = x // m.pow(10, len(str(x))-1)
while x > 0:
    count += 1
    x = x // 10
print(f"X có {count} chữ số")
print("Chữ số đầu tiên của X:", int(first_num))

