# 2. Bạn có 10 triệu đồng trong tài khoản ngân hàng, với lãi xuất 5,1% hàng năm. Tính xem: • Sau 10 năm bạn có bao nhiêu tiền? • Sau bao nhiêu năm bạn sẽ có ít nhất 50 triệu đồng?
so_tien = 1e7
lai_suat = 0.051
so_nam = 0

so_tien_sau_10_nam = so_tien * ((1 + lai_suat)**10)
print("Sau 10 năm bạn có ", so_tien_sau_10_nam)

while so_tien < 5e7:
    so_nam += 1
    so_tien = so_tien * (1 + lai_suat)
    print(f"Số tiền sau {so_nam} năm: {so_tien:.2f} vnd")
print("Sau",so_nam,"năm bạn sẽ có ít nhất 50 triệu")