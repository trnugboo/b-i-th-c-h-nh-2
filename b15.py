doan_van = input("Nhập một đoạn văn: ")
tu = doan_van.translate(str.maketrans("", "", ".,!?" )).lower().split()

tan_suat = {}
for tu_vung in tu:
    tan_suat[tu_vung] = tan_suat.get(tu_vung, 0) + 1

sap_xep = sorted(tan_suat.items(), key=lambda muc: muc[1], reverse=True)
print("Danh sách từ theo tần suất giảm dần:")
for tu_vung, so_lan in sap_xep:
    print(f"{tu_vung}: {so_lan}")
