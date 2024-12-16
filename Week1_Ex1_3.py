# 1. Gõ 3 ví dụ phía trước vào 3 file, đặt tên đuôi .py, sau đó sử dụng trình thông dịch python để chạy thử xem kết quả ra sao
a = int(input("A = "))

b = int(input("B = "))

while (b > 0):
    if (a > b):
        a, b = b, a % b
    else:
        a, b = a, b % a
print("Ước số chung lớn nhất là:", a)