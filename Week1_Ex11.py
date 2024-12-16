# 6. Viết chương trình nhập số nguyên dương N và tính giá trị hàm F(N) dưới đây F(N)=1!2! + ... + N!
def gt(n):
    if n == 1 or n == 0:
        return 1
    return n*gt(n-1)

def calc(n):
    result = 1
    i = 1
    while i <= n:
        result *= gt(i)
        i += 1
    return result
n = int(input("Nhập số nguyên dương N: "))
print(f"F(N) = {calc(n)}")