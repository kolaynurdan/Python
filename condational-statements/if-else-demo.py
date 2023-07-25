#1- ..

name = input('Name: ')
age = int(input('Age: '))
training = input('Training: ')

if (age>=18): 
    if (training == 'done' or training == 'will done'):
        print(f'{name} are a driver')
    else:
        print(f'{name} are not driver')
else:
    print(f'{name} are not driver beacause of age.')


#2- Get 2 midterms(%60) and 1 final grade(%40) from the user and calculate the average.

midterm1 = float(input('Midterm1: '))
midterm2 = float(input('Midterm2: '))
final = float(input('final: '))

avrg = (midterm1+midterm2+final)/3

if(avrg>=0) and (avrg<25):
    print(f'Average: {avrg} Grade=0')
elif (avrg>=25) and (avrg<45):
    print(f'Average: {avrg} Grade=1')
elif (avrg>=45) and (avrg<55):
    print(f'Average: {avrg} Grade=2')
elif (avrg>=55) and (avrg<70):
    print(f'Average: {avrg} Grade=3')
elif (avrg>=70) and (avrg<85):
    print(f'Average: {avrg} Grade=4')
elif (avrg>=85) and (avrg<=100):
    print(f'Average: {avrg} Grade=5')
else:
    print('The information is wrong!')

#3- ..

import datetime

tdate = input('"How many days(yyyy/mm/dd) has your car been on the road?')
tdate = tdate.split('/')
#print(tdate[0])
#print(tdate[1])
#print(tdate[2])

onTraffic = datetime.datetime(int(tdate[0]),int(tdate[1]),int(tdate[2]))
tnow = datetime.datetime.now()

difference = tnow - onTraffic
dayss = difference.days
print(dayss)