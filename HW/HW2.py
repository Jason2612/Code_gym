so_nguyen = int(input("Nhap chuoi so 3 chu so: "))

tong_chu_so_chan = 0
tong_chu_so_le = 0

while so_nguyen > 0:
    if so_nguyen % 2 != 0:
        tong_chu_so_le += so_nguyen % 10
        so_nguyen = so_nguyen // 10
    else:
        tong_chu_so_chan += so_nguyen % 10
        so_nguyen = so_nguyen // 10
    

print(tong_chu_so_le)
