number = float(input('Please enter a number: '))

if (number>0) and (number<=100):
    print('the number is 0-100 range.')
else:
    print('the number is not 0-100 range.')


number2 = int(input('Please enter a number: '))
if (number2 > 0):
    if (number2%2==0):
        print('positive even number')
    else:
        print('It is not positive number')
else:
    print('not positive even number')



email = 'nurdan@gmail.com'
password = 'abc123'

enteredEmail = input('Email: ')
enteredPassword = input('Pass: ')

if(enteredEmail == email):
    if (enteredPassword == password):
        print('you entered successfully.')
    else:
        print('wrong password')
else:
    print('wrong email')

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a>b) and (a>c):
    print(f'a is greater than others.')
elif (b>a) and (b>c):
    print(f'b is greater than others.')
elif (c>a) and (c>b):
    print(f'c is greater than others.')