# Ham lambda
"""
x = lambda a,b : a + b
print(x(4,6))
"""

# Ham de quy
"""
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

rs = sum(5)
print(rs)
"""
# Bai tap tinh giai thua
"""
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n-1)

rs = giaiThua(5)
print(rs)
"""

# Fibonaci
"""
def fibonaci(n):
    if n == 1 or n == 2:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(8))
"""

# sap xep so dung phep chia du
my_str = "32242491"
# Tìm ra số lớn nhất
# Loại bỏ số đó ra khỏi chuỗi
# Lặp lại cho đến khi chuỗi bằng 0

rs = ""
while len(my_str) != 0:
    max = 0
    pos = 0
    max_pos = pos
    while pos < len(my_str):
        if int(my_str[pos]) >= max:
            max = int(my_str[pos])
            max_pos = pos
        pos += 1
    my_str = my_str[:max_pos] + my_str[max_pos+1:]
    rs = rs + str(max)
