person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    vi_tri_giua = len(skills) // 2
    print(skills[vi_tri_giua])

if 'skills' in person:
    if 'python' in person['skills']:
        print('Co ky nang python')
    else:
        print('Khong co ky nang python')
if 'skills' in person:
    skills = person['skills']

    if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')

    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')

    elif 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')

    else:
        print('unknown title')
if person['is_married'] == True and person['country'] == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. "
        f"He is married."
    )