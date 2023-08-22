def changeName(n):
    n = 'ada'

name='yigit'

changeName(name)

print(name)

def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara','izmir']

change(sehirler)

print(sehirler)

def add(a,b,c=0):
    return sum((a,b,c))

print(add(10,20))
print(add(10,20,30))

def addd(*params):
    return sum(params)

print(addd(10,20))
print(addd(10,20,30))
print(addd(10,30,60,90))

def adddd(*params):
    sum = 0

    for n in params:
        sum = sum + n

    return sum

print(adddd(10,20))
print(adddd(10,20,30))
print(adddd(10,30,60,90))