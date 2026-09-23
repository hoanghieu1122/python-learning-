ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages[0])
print(ages[-1])

max_ages = ages[-1]
min_ages = ages[0]
ages.append(max_ages)
ages.append(min_ages)
print(ages[len(ages) // 2])
tuoitb = sum(ages)/len(ages)
print(tuoitb)
chenhlech = max_ages - min_ages
min_distance = abs(min_ages - chenhlech)
max_distance = abs(max_ages - chenhlech)
print(min_distance > max_distance)