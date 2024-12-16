"""
9. Nhập vào từ bàn phím thông tin về ngày X, bằng cách nhập ba số nguyên dương d, m và y
lần lượt là giá trị ngày (d) tháng (m) năm (y) của X. Tính và in ra ngày tiếp sau của X
Ví dụ: người dùng nhập d = 31, m = 1, y = 2019 (tức X là ngày 31 tháng 1 năm 2019) thì chương trình cần in ra 1/2/2019
"""
thang_du = [1, 3, 5, 7, 8, 10, 12]
thang_thieu = [4, 6, 9, 11]
def tinh_ngay(d,m,y):
    if d == 31:
        if m == 12:
            y += 1
            d = 1
        if m in thang_du[:6]:
            m += 1
            d = 1
    elif d == 30 and m in thang_thieu:
        m += 1
    elif d == 29 and m == 2 and y % 4 == 0:
        d = 1
        m += 1
    elif d == 28 and m == 2 and y % 4 != 0:
        d = 1
        m += 1
    else:
        d += 1
    return f"{d}/{m}/{y}"

def is_available_day(d,m,y):
    if d > 0:
        if d <= 31 and m in thang_du:
            return True
        elif d <= 30 and m in thang_thieu:
            return True
        elif d <= 29 and m == 2 and y % 4 == 0:
            return True
        elif d <= 28 and m == 2 and y % 4 != 0:
            return True
    return False
d, m, y = list(map(int, input("Nhập ngày tháng năm: ").split()))
print(f"Ngày tiếp theo là: {tinh_ngay(d,m,y)}" if is_available_day(d,m,y) else "Ngày nhập không hợp lệ")