def sayHello():
    print('Hello')

sayHello()
sayHello()
sayHello()


def sayHello(name):
    print('Hello '+name)

sayHello('Nurdan')
sayHello('Nuray')
sayHello('Ayse')


def sayHello3(name = 'user'):
    return 'Hello '+name

msg = sayHello3('Nurdan')

print(msg)

def total(num1,num2):
    return num1+num2

result = total(10,20)
print(result)

def AgeCal(birthDate):
    resultt = 2023 - birthDate
    print(result)