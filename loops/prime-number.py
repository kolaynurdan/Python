number = int(input('Number: '))
primeNumber = True

if (number == 1):
    primeNumber = False

for i in range(2, number):
    if number % i == 0:
       primeNumber = False
       break

if primeNumber:
    print('prime number')
else:
    print('not prime number')