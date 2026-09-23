a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
pheptinh = input("Nhap phep tinh: ")
if pheptinh == "+":
    print(a+b)
elif pheptinh == "-":
    print(a-b)
elif pheptinh =="*":
    print(a*b)
elif pheptinh == "/":
    if b == 0:
        print("Ko chia đc voi 0")
    else:
        print (a/b)
