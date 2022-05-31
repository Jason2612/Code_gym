import turtle

t = turtle.Turtle()

n = int(input("Nhap 1 con so ban muon: "))
while n > 0:
    t.forward(100)
    t.right(90)
    n -= 1

turtle.done

# so_nguyen = int(input("Nhap chuoi so 3 chu so: "))

# tong_chu_so_chan = 0
# tong_chu_so_le = 0

# while so_nguyen > 0:
#     if so_nguyen % 2 != 0:
#         tong_chu_so_le += so_nguyen % 10
#         so_nguyen = so_nguyen // 10
#     else:
#         tong_chu_so_chan += so_nguyen % 10
#         so_nguyen = so_nguyen // 10
    

# print(tong_chu_so_le)0

# so_nguyen = int(input("Nhap chuoi so: "))

# tong_cac_chu_so = 0

# while so_nguyen > 0:
#     tong_cac_chu_so += so_nguyen % 10
#     so_nguyen = so_nguyen // 10

# print(tong_cac_chu_so)

