danh_sach_1 = [int(so) for so in input("Nhập danh sách thứ nhất: ").split()]
danh_sach_2 = [int(so) for so in input("Nhập danh sách thứ hai: ").split()]

danh_sach_gop = sorted(danh_sach_1 + danh_sach_2)
print("Danh sách sau khi gộp và sắp xếp:", danh_sach_gop)
