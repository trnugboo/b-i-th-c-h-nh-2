chuoi_so = input("Nhập danh sách số: ").split()

if chuoi_so:
    danh_sach = [int(so) for so in chuoi_so]
    tong_chan = sum(so for so in danh_sach if so % 2 == 0)
    print("Tổng các số chẵn:", tong_chan)
else:
    print("Danh sách không có phần tử.")
