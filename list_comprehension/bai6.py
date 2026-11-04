names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]

result = [
    firt + " " + last
    for row in names
    for firt ,last in row
]
print (result)