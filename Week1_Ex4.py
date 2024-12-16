# 4. Nhập 2 số nguyên a và b, hãy tính và in ra căn bậc b của a
import math as m
a = int(input("Nhập số A: "))
b = int(input("Nhập số B: "))
print("Căn bậc B của A = ", m.pow(a, 1/b))