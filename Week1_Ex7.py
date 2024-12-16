# 2. Viết hàm area trả về diện tích tam giác khi biết độ dài ba cạnh của chúng
import math as m
def area(a,b,c):
    p = (a+b+c)/2
    return m.sqrt(p*(p-a)*(p-b)*(p-c))
a = int(input("Nhập độ dài cạnh 1: "))
b = int(input("Nhập độ dài cạnh 2: "))
c = int(input("Nhập độ dài cạnh 3: "))
if(a+b>c and a+c>b and b+c>a): print("Diện tích tam giác: ",area(a,b,c))
else: print("3 cạnh nhập vào không hợp lệ")