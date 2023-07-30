#1-100

x = 0

while x<100:
    print(x) 
    x = x + 1

print('This is over')

x = 1 
while x <= 100:
    if x%2 == 1:
        print(f'odd number: {x}')
    else:
        print(f'even number: {x}')
    x += 1

print('this is over..')

name = '' #False
while not name:
    name = input('Enter your name: ')

print(f'Hello, {name}')