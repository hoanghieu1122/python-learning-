diem = int(input('Nhap diem'))

if diem >= 90 :
    print('A')
elif diem >=80 and diem < 90 :
    print('B')
elif diem >=70 and diem < 80 :
    print('C')
elif diem >=60 and diem < 70 :
    print('D')
else:
    print('F')
#2
thang = int(input('Nhap thang: '))

if thang < 4 and thang > 0:
    print("Mua Xuan")
elif thang < 7 :
    print('Mua Ha')
elif thang < 10:
    print('Mua Thu')
else:
    print('Mua Dong')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
trai_cay = input("Nhap trai cay")
if trai_cay in fruits:
    print('Da ton tai')
else:
    fruits.append(trai_cay)
    print(fruits)