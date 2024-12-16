"""
7. Viết chương trình nhập điểm trung bình học tập của một sinh viên,
sau đó dựa trên quy tắc dưới đây in ra đánh giá kết quả học tập của sinh viên đó.
• Điểm dưới 3.5: xếp loại yếu
• Điểm từ 3.5 đến dưới 5: xếp loại kém
• Điểm từ 5 đến dưới 6.5: xếp loại trung bình
• Điểm từ 6.5 đến dưới 8: xếp loại khá
• Điểm từ 8 đến dưới 9: xếp loại giỏi
• Điểm từ 9 trở lên: xếp loại xuất sắc
"""

def danh_gia(dtb):
    if dtb < 3.5:
        return "Yếu"
    if dtb >= 3.5 and dtb < 5:
        return "Kém"
    if dtb >= 5 and dtb < 6.5:
        return "Trung bình"
    if dtb >= 6.5 and dtb < 8:
        return "Khá"
    if dtb >= 8 and dtb < 9:
        return "Giỏi"
    if dtb >= 9 and dtb <= 10:
        return "Xuất sắc"

dtb = float(input("Nhập điểm trung bình: "))
print(f"Xếp loại học tập: {danh_gia(dtb)}" if (dtb >= 0 and dtb <= 10) else "Điểm trung bình nhập vào không hợp lệ")