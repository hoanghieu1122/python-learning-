import string
import random


def user_if_gen_by_user():
    so_ky_tu = int(input('Nhap ky tu cua moi id'))
    so_luong = int(input('Nhap luong if can tao'))
    
    ky_tu = string.ascii_letters + string.digits

    for i in range(so_luong):
        user_id = ''
        for j in range(so_ky_tu):
            user_id += random.choice(ky_tu)
        print(user_id)

user_if_gen_by_user()