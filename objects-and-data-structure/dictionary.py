# key - value 

#41 - Kocaeli 34 - Istanbul

cities = ['Kocaeli', 'Istanbul']
cityCode = [41,34]

print(cityCode[cities.index('Kocaeli')])

#cityCode = { 'key': value }
cityCode = { 'Kocaeli': 41 , 'Istanbul' : 34 }

print(cityCode['Kocaeli'])
print(cityCode['Istanbul'])

cityCode['Ankara'] = 6

print(cityCode)

cityCode['Kocaeli'] = 'new value'

print(cityCode)

users = {
    'nurdankolay' : {
        'age' : 30,
        'email' : 'nurdan@gmail.com',
        'roles' : ['admin', 'user']
    },
    'nuraykolay' : {
        'age' : 33,
        'email' : 'nuray@gmail.com',
        'roles' : ['user']
    },
}

print(users)
print(users['nurdankolay']['age'])