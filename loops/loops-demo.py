import random

number = random.randint(1,100)
right = 5

while right > 0:
    right -=1
    guess = int(input('Guess: '))

    if number == guess:
        print('Congrats!')
        break
    elif number > guess:
        print('up')
    elif number < guess:
        print('down')
    if right == 0:
        print('you dont have any right. Number: {number}')