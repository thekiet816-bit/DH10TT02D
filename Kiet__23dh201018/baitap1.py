# Nhập điểm trung bình từ bàn phím (ép kiểu sang số thực float)
dtb = float(input("Nhập điểm trung bình: "))

# Kiểm tra điều kiện để xếp loại
if dtb >= 8:
    print("Gioi")
elif 6.5 <= dtb < 8:
    print("Kha")
elif 5 <= dtb < 6.5:
    print("Trung binh")
else:
    print("Yeu")