# 3. Viết hàm area2 trả về diện tích tam giác biết tọa độ (x, y) của ba đỉnh tam giác
import math as m
def area2(x1,y1,x2,y2,x3,y3):
    return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))/2
def get_distance(x1,y1,x2,y2):
    return m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
point1 = list(map(int, input("Nhập tọa độ đỉnh A: ").split()))
point2 = list(map(int, input("Nhập tọa độ đỉnh B: ").split()))
point3 = list(map(int, input("Nhập tọa độ đỉnh C: ").split()))

x1, y1 = point1
x2, y2 = point2
x3, y3 = point3

AB = get_distance(x1,y1,x2,y2)
BC = get_distance(x2,y2,x3,y3)
AC = get_distance(x1,y1,x3,y3)

if(AB + BC > AC and AB + AC > BC and BC + AC > AB): print("Diện tích tam giác:",area2(x1,y1,x2,y2,x3,y3))
else: print("Tọa độ 3 đỉnh không tạo thành 1 tam giác")