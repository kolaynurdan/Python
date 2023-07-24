name = input('Name: ')
age = input('Age: ')
training = input('Training: ')

if (age >= 18):
    if (training == 'will done' or training == 'done'):
        print(f'{name} will get a driver licence.')
    else:
        print(f'{name} wont get a driver because of training.')
else:
    print(f'{name} wont get a driver licence because of age')