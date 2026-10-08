import random

def random_numbers():
    danh_sach = []

    while len(danh_sach) < 7:
        so = random.randint(0,9)
        if so not in danh_sach:
            danh_sach.append(so)

    return danh_sach
print(random_numbers())