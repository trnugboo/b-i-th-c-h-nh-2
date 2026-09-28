chuoi_english = input("Nhập chuỗi tiếng Anh: ")
nguyen_am = "aeiou"
so_nguyen_am = 0
so_phu_am = 0
for ky_tu in chuoi_english.lower():
	if ky_tu.isalpha():
		if ky_tu in nguyen_am:
			so_nguyen_am += 1
		else:
			so_phu_am += 1

print("Số lượng nguyên âm:", so_nguyen_am)
print("Số lượng phụ âm:", so_phu_am)
