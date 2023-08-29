x = input('1. number: ')
y = input('2. number: ')

toplam = int(x)+int(y)

print(toplam)

x = 5 
y = 2.5
name = 'Nuray'
isOnline = True

# Type Conversion

# int to float

x = float(x)

print(x)
print(type(x))

#float to int

y = int(y)

print(y)
print(type(y))

#integer or float to string

result = str(x) + str(y)
print(result)
print(type(result))

#bool to str

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

#bool to int

isOnline = True
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))

'''

circumference of the circle : pi*r*r

area of the circle : 2*pi*r

Calculate the circumference and area of a circle with a given radius.(pi=3.14)

'''

pi = 3.14

radius = float(input ("you can enter a radius: "))
area = pi*(radius**2)
circumference = 2 *pi*radius
print('circumference: '+ str(circumference)+'area: '+ str(area))