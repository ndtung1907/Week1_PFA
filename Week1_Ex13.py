"""
8. Nhập vào từ bàn phím ba số a, b và c. Thực hiện các công việc dưới đây:
• In ra màn hình giá trị lớn nhất trong ba số
• Nếu có ít nhất hai số cùng nhận giá trị lớn nhất, in ra giá trị thứ ba còn lại
"""

a, b, c = list(map(int, input("Nhập vào 3 số a, b, c: ").split()))
max0 = max(a, b, c)
print("Số lớn nhất trong 3 số:", max0)
if (a == b and b == max0):
    print("Số còn lại:",c)
if (b == c and c == max0):
    print("Số còn lại:", a)
if (a==c and c ==max0):
    print("Số còn lại:",b)