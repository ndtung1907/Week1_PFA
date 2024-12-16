# 1. Gõ 3 ví dụ phía trước vào 3 file, đặt tên đuôi .py, sau đó sử dụng trình thông dịch python để chạy thử xem kết quả ra sao
def giaithua(n):
    gt = 1
    for i in range(2, n+1):
        gt = gt * i
    return gt

a = int(input("Nhập giá trị n: "))

print("N! =", giaithua(a))