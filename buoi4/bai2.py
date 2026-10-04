a = {'ff', 'Lq'}
b = {'freefire' , 'Lien Quan'}
# ket hop
print(a.union(b))
# tim giao cua A va B
print(a.intersection(b))
# a co phai tap con cua b hay khong
print(a.issubset(b))
# a va b co phai la tap hop roi nhau hay khong
print(a.isdisjoint(b))
