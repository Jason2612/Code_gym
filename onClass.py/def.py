
# def cong_hai_so(so1:int, so2:int)-> int:
#     print(so2)

# cong_hai_so(so2 = 1, so1 = 2)

#default paramater
# chi bat buoc gan cho parameter cuoi
# khi nhap argument thi se lay gia tri nhap 

"""
Arbitrary Argument, *args
khi minh khong biet truyen vao bao nhieu arguments
hoac minh tao ham nhung khong biet co bao nhieu paramater
"""

# def tong_n_so(*dsso):
#     for so in dsso:
#         print(so)
# tong_n_so(1,2,3,4,5,6,7,8)

"""
Arbitrary Keyword Argument, **kargs
"""
# def test(**ds):
#     print(ds['phongpc'])

# test(phongpc = 1)


"""
Ham swap
"""

# def swap(so1, so2):
#     tmp = so1
#     so1 = so2
#     so2 = tmp
#     print("bên trong hàm")
#     print(so1, so2)

# number1 = 1
# number2 = 2

# print(number1, number2)
# swap(number1, number2)
# print(number1, number2)

"""
Bien toan cuc va cu bo
"""
# x = 5 # global variables

# def test():
#     # Local variables
#     i = 1
#     print(x)
#     for z in 'abc':
#         print(z)
#         print(x)

# test()

"""
global
"""

# x = 5
# def test():
#     global x
#     x = 0 
#     print(x)

# test()
# print(x)

age = 18
def tang_do_tuoi(age):
    return age + 5

age = tang_do_tuoi(age)
print(age)