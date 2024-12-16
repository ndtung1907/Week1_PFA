# 1. Viết hàm average nhận 5 tham số và trả về giá trị trung bình cộng của chúng
def average(*numbers):
    return sum(numbers) / len(numbers)
print(average(1,2,3,4,5))