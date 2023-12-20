#error handling 

'''
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('You cant enter 0 for y')
except ValueError:
    print('you have to enter digit value for x and y')
'''

try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError,ValueError) as a:
    print('You enter wrong value!')
    print(a)
else:
    break