#x = 5 

#y = 10 

#z = 20

x,y,z = 5, 10 , 25

print(x,y,z)

x, y = y, x

print(x,y,z)

x +=5 #x=x+5
x -=5 #x=x-5
x *=5 #x=x*5

print(x,y,z)

values = 1,2,3,5,6

print(values)
print(type(values))

a, b, *c = values

print(a,b,c)

print(a,b,c[1])


