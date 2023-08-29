#1 - Which of the two numbers entered is greater?

a = int(input('Please enter a number: '))
b = int(input('Please enter another number: '))

result = (a > b)
print(f'a: {a} is grater than b: {b} : {result}')

#2- Get 2 midterms(%60) and 1 final grade(%40) from the user and calculate the average.

midterm1 = float(input('Midterm1: '))
midterm2 = float(input('Midterm2: '))
final = float(input('final: '))

averageGrade = ((midterm1+midterm2)/2*0.6) + ((final) * 0.4)
print(f'Grade Average: {averageGrade} and you pass or fail this lesson: {averageGrade>=50}')

#3- Print whether the entered number is an odd number or an even number.

c = int(input('Please enter a number: '))
oddOrEven = (c % 2 == 0)
print(f'the evenness of the entered number: {oddOrEven}')

#4- Print the positive/negative status of the entered number.

d = int(input('Please enter a number: '))
orPositive = (d>0)

print(f'The positivity or negativity status of the entered number: {orPositive}')

#5- Request email and password and validate their correctness.

email = 'nurdan@gmail.com'
password = 'abc123'

enteredEmail = input('email: ')
enteredPassword = input('password: ')

isEmail = (email == enteredEmail)
isPassword = (password == enteredPassword)

print(f'Is the email correct?: {isEmail}')
print(f'Is the password correct?: {isPassword}')