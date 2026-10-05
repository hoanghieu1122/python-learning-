dog = {}

dog['name'] = 'hehe'
dog['color'] = 'brown'
dog['legs'] = '4'
dog['age'] = '2'

student = {}

student['first_name'] = 'Hieu'
student['last_name'] = 'Vo'
student['gender'] = 'Nam'
student['martial_status'] = 'Doc than'
student['skills'] = 'python'
student['country'] = 'Viet Nam'
student['city'] = 'Da Nang'
student['address'] = 'Tran Van On'
print(len(student))
hehe = student['skills']
print(type(list(hehe)))

student['skills'].append('Free Fire')
list(student.keys())
list(student.values())
student.items()
student.pop('age')
del dog