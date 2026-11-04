countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

result = [
    [contry.upper(),contry[:3].upper(),city.upper()]
    for row in countries
    for contry,city in row
]
print(result)