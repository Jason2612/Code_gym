

nam = int(input("Nhap so nam: "))
if nam >= 0:
    if nam % 4 == 0 and nam % 100 != 0:
        print("Nam nhuan")
    elif nam % 100 == 0 and nam % 400 == 0:
        print("Nam nhuan")
    else:
        print("Khong phai nam nhuan")
else:
    print("Error")
    