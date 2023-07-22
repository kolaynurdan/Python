x,y,z = 2,5,10

numbers = 1,5,7,10,6

#1- The difference between the 2 numbers entered by the user and the sum of x, y, z?
#a = int(input('Please enter a number: '))
#b = int(input('Please enter a number: '))

#result = (a*b) - (x+y+z)
#print(result)

#2- dividing y by x without a remainder

result2 = y // x
print(result2)

#3-What is the mod 3 result of the sum (x,y,z) ?

result3 = (x+y+z)%3
print(result3)

#4- y to the xth power

result4 = y**x
print(result4)

#5- x, *y, z = numbers What is z to the 3rd power?

numbers = 1,5,7,10,6
x, *y, z = numbers

print(x, *y, z)

#6-  x, *y, z = numbers, sum of y values?

numbers = 1,5,7,10,6
x, *y, z = numbers

sum = y[0]+y[1]+y[2]
print(sum)