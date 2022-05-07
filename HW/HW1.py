a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
c = int(input("Nhap so nguyen c: "))

if a >= b and a >= c:
    print(a)
else:
    if b >= a and b >= c:
        print(b)
    else:
        print(c)
