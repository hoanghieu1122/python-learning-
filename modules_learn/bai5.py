import random


n = int(input('Nhap so luong mau RGB'))

def list_of_rgb_color(n):
    danh_sach = []
    for i in range(n):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        mau = f"rgb({r},{g},{b})"
        danh_sach.append(mau)
    return danh_sach
print(list_of_rgb_color(n))

    