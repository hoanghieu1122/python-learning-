countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

result = [
     {'country': country.upper(), 'city': city.upper()}
     for row in countries
     for country, city in row
]
print (result)