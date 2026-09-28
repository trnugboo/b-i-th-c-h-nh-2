danh_sach = [int(so) for so in input("Nhập danh sách số: ").split()]
danh_sach_lon_hon_10 = [so for so in danh_sach if so > 10]

print("Danh sách các số lớn hơn 10:", danh_sach_lon_hon_10)
