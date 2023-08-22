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
    return 2023 - birthDate


ageNurdan = AgeCal(1993)
ageNuray = AgeCal(1993)
ageAyse = AgeCal(1993)

print(ageNurdan,ageNuray,ageAyse)

def HowManyYearRemain(birthDate, name):
    yas = AgeCal(birthDate)
    rremains = 65 - yas

    if rremains > 0 :
        print(f'Remains:  {rremains} ')
    else:
        print('you are retired!')

HowManyYearRemain(1993,'Esma')