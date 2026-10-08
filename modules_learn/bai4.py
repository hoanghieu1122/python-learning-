import random

n = int(input('Nhap so luong mau hex nhau nhien: '))
def list_of_hexa_colors(n):
    ky_tu = '0123456789abcdef'
    danh_sach =  []

    for i in range(n):
        mau = '#'
        for j in range(6):
            mau += random.choice(ky_tu)

        danh_sach.append(mau)
    return danh_sach

print(list_of_hexa_colors(n))