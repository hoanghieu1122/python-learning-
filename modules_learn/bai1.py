import random
import string

def random_user_id():
    ky_tu = string.ascii_letters + string.digits
    user_id = ''

    for i in range(6):
        user_id += random.choice(ky_tu)

    return user_id

print(random_user_id())