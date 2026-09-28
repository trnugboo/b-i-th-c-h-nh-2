chuoi_so = input("Nhập danh sách số: ").split()

if chuoi_so:
    danh_sach = [int(so) for so in chuoi_so]
    phan_tu_nhieu_nhat = danh_sach[0]
    so_lan_nhieu_nhat = danh_sach.count(phan_tu_nhieu_nhat)

    for so in danh_sach[1:]:
        so_lan = danh_sach.count(so)
        if so_lan > so_lan_nhieu_nhat:
            phan_tu_nhieu_nhat = so
            so_lan_nhieu_nhat = so_lan

    print("Phần tử xuất hiện nhiều nhất:", phan_tu_nhieu_nhat)
    print("Số lần xuất hiện:", so_lan_nhieu_nhat)
else:
    print("Danh sách không có phần tử.")
