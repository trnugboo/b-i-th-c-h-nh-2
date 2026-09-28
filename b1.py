chuoi = input("Nhập chuỗi: ")
print("Độ dài chuỗi:", len(chuoi))
tan_suat = {}
for ky_tu in chuoi:
	tan_suat[ky_tu] = tan_suat.get(ky_tu, 0) + 1
print("Số lần uất hiện của mỗi ký tự:")
for ky_tu, so_lan in tan_suat.items():
	ten_ky_tu = "dấu cách" if ky_tu == " " else ky_tu
	print(f"'{ten_ky_tu}': {so_lan}")
