list = []

lista = ['1', 2 , 3 , 'hehe' , '03412233444' , 'hoang hieu']

print(len(lista))
print(lista[0] + lista[3] +  lista[5])

mixed_data_types = ['name', 'age' , 'height', 'marital' ,'status','address']

it_companies = ['Facebook' , 'Google' , 'Microsoft' , 'Apple' , 'IBM','Oracle','Amazon']

print(it_companies)
print(len(it_companies))
it_companies.append('Free Fire')
it_companies.insert(4,'PUPG')
it_companies[0] = it_companies[0].upper()
print(it_companies[0])
print('#;'.join(it_companies))
print('Microsoft' in it_companies)
it_companies.sort() #Tang Dan
print(it_companies)
it_companies.reverse()
print(it_companies)
del it_companies[:3]
print(it_companies)
del it_companies[-3:]
print(it_companies)
del it_companies[len(it_companies) // 2]
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.append(back_end)
fullstack = front_end.copy()
print(fullstack)
