tong = 0
for i in range(101):
    tong += i
print(tong)
tong_le = 0
tong_chan = 0
for i in range(101):
    if(i % 2 == 0):
        tong_chan += i
    else:
        tong_le += i

print(tong_le)
print(tong_chan)