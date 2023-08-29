#1- Check if the entered number is between 0 and 100

a = float(input('Please enter a number: '))

result = (a > 0) and (a <=100)
print(f'Is this number in 0-100 range?: {result} ')

#2- Check if the entered number is positive and even.

b = float(input('Please enter a number: '))

result = (b > 0) and (b % 2 == 0)
print(f'entered number is positive and even? : {result}')

#3- Perform login authentication using email and password information.
email = 'nurdan@gmail.com'
password = 'abc123'

enteredEmail = input('please enter your email: ')
enteredPassword = input('please enter your password: ')

result = (email == enteredEmail) and (password == enteredPassword)
print(f'Is this correct login?: {result}')

#4- Let's compare the 3 entered numbers in terms of magnitude.

a = int(input('a number: '))
b = int(input('b number: '))
c = int(input('c number: '))


result = (a > b) and (a > c)
print(f'a is greater than anothers: {result}')

result = (b > a) and (b > c)
print(f'b is greater than anothers: {result}')

result = (c > b) and (c > a)
print(f'c is greater than anothers: {result}')

#5- Get 2 midterms(%60) and 1 final grade(%40) from the user and calculate the average.

midterm1 = float(input('Midterm1: '))
midterm2 = float(input('Midterm2: '))
final = float(input('final: '))

averageGrade = ((midterm1+midterm2)/2)*0.6 + (final)*0.4

result = (averageGrade>=50) and (final>=50)

print(f'Student average grade: {averageGrade} and pass or fail : {result}')

#6- To calculate the Body Mass Index (BMI) based on a person's name, weight, and height, you can use the following English expression:

#"Calculate the Body Mass Index (BMI) based on the person's name, weight, and height."

#BMI is calculated using the formula: BMI = weight (kg) / height^2 (m^2)

name = input('Name: ')

kg = float(input('Kilogram: '))

hg = int(input('Height: '))

index = (kg) / (hg**2) 

thin = (index >= 0 ) and (index <= 18.4 )
normal = (index >= 18.4) and (index <= 24.9)
chubby = (index >= 24.9) and (index <= 29.9)
fat = (index >= 29.9) and (index <= 34.9)

print(f'{name} kilo index: {kg} and Body Mass Index (BMI)(thin): {thin}')
print(f'{name} kilo index: {kg} and Body Mass Index (BMI)(normal): {normal}')
print(f'{name} kilo index: {kg} and Body Mass Index (BMI)(chubby): {chubby}')
print(f'{name} kilo index: {kg} and Body Mass Index (BMI)(fat): {fat}')