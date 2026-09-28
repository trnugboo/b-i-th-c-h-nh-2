chuoi_so = input("Nhập danh sách số nguyên: ")
if chuoi_so.strip():
	danh_sach = [int(so) for so in chuoi_so.split()]
	print("Tổng:", sum(danh_sach))
	print("Trung bình:", sum(danh_sach) / len(danh_sach))
	print("Số lớn nhất:", max(danh_sach))
else:
	print("Danh sách không có phần tử.")





