age = int(input('enter your age: '))
age_du = 18 - age
if age > 18 :
    print('Du tuoi hoc bang lai xe')
else:
    print(f'Can cho them {age_du} nam de hoc bang lai xe')

#2
my_age = int(input('Enter your age: '))
your_age = int(input('Enter you age: '))

if my_age > your_age:
    print('my_age')
    lech = my_age - your_age
    if lech == 1 :
        print('lech 1 year')
    else:
        print(f'lech {lech} years')
elif my_age < your_age:
    print('your_age')
    lech = your_age - my_age
    if lech == 1 :
        print('lech 1 year')
    else:
        print(f'lech {lech} years')
else:
    print('2 dua bang nhau')

