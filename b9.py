danh_sach = [int(so) for so in input("Nhập danh sách các số: ").split()]
danh_sach_khong_trung = []
for so in danh_sach:
	if so not in danh_sach_khong_trung:
		danh_sach_khong_trung.append(so)
print("Danh sách sau khi loại bỏ phần tử trùng:", danh_sach_khong_trung)
