# n = int(input("Nhap so n: "))
# for i in range(0, n):
#     for a in range(0, i+1):
#         print("*", end="")
#     print("\r")

# n = int(input("Nhap so n: "))
# for i in range(n, 0, -1):
#     for a in range(i, 0, -1):
#         print("*", end="")
#     print("\r")

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(str(i) + " x " + str(j) + " = " + str(i*j))

# a = int(input("Nhap 1 so nguyen duong: "))
# print(str(a)[0])




a = int(input("Nhap 1 so nguyen duong: "))
total = 0
while total <= len(str(a)):
    current_number = a // 10
    current_number = current_number // 10
    current_digit = int(str(a)[0])
    print(current_number)
    total += 1
    if current_digit == current_number:
        break
    





