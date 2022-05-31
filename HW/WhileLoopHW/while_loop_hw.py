# Nhập một chuỗi số. nhập số nguyên dương n. Tìm vị trí đầu tiên của số đó

# a = input("Nhap 1 chuoi so: ")
# soCanTimVitri = input("Nhap so trong chuoi da nhap: ")
# for i in a:
#     if i == soCanTimVitri:
#         print(a.index(i))

# Nhập một chuỗi nhiều từ -> đếm xem có bao nhiêu từ trong chuỗi

# nhapChuoi = input("Nhap 1 cau bat ki: ")
# for i in nhapChuoi:
#     a = nhapChuoi.count(" ") + 1
# print("Tong so tu trong chuoi da nhap: " + str(a))

"""
Viết chương trình tính n giai thừa
Nhập n -> tính n giai thừa
"""

# n = int(input("Nhap 1 so nguyen bat ki lon hon 0: "))
# a = 1
# if n > 0:
#     for i in range(1, n+1):
#         a *= i
# print(a)

"""
Viết chương trình kiểm tra số đó có phải là số nguyên tố hay không
"""

# n = int(input("Nhap 1 so nguyen bat ki"))

# for j in range(0, n+1):
#     result = True
#     if j < 2:
#         result = False
#     elif j == 2:
#         result = True
#     elif j % 2 == 0:
#         result = False
#     else:
#         for i in range(3, j, 2):
#             if j % i == 0:
#                 result = False
#     if result == True:
#         print(j)

"""
Nhập 2 số a, b
In ra các số nguyên tố nằm trong khoảng đó
"""


# a = int(input("Nhap 1 so nguyen: "))
# b = int(input("Nhap 1 so nguyen: "))

# for i in range(a, b+1):
#     result = True
#     if i < 2:
#         result = False
#     elif i == 2:
#         result = True
#     elif i % 2 == 0:
#         result = False
#     else:
#         for j in range(3, i, 2):
#             if i % j == 0:
#                 result = False
#     if result == True:
#         print("Day la cac so nguyen to: " + str(i))

"""
Nhập một chuỗi số : “32242491” 
Sắp xếp chuỗi theo thứ tự từ bé đến lớn 
Sắp xếp chuỗi theo thứ tự từ lớn đến bé
"""




# chuoiSo = "32242491"

# for i in chuoiSo:
#     for j in chuoiSo:

#         count = 0
#         while count <= len(chuoiSo):
#             if i <= j:
#                 so1 = i
#             elif i < j:
#                 so2 = i
#             count += 1

# print(so1 + so2)


"""
Cho một chuỗi số “134513515”
In ra màn hình tất cả cặp số (2 số ) có tổng = 10 ( 6-4 tương đương 4-6 -> chỉ in một lần )
"""


# chuoiSo = "134513515"

# for i in chuoiSo:
#     for j in chuoiSo:
#         if int(i) + int(j) == 10:
#             result = True
# if result == True:
#     print(i + "-" + j)

"""
Nhập một số kiểm tra số đó có phải số hoàn hảo không ( số hoàn hảo bằng tổng ước số của nó không bao gồm nó )
"""



n = int(input("Nhap 1 so nguyen duong: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print("Day la so hoan hao: " + str(n))
else:
    print("Day khong phai la so hoan hao!")
