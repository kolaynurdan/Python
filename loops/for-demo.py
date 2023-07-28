numbers = [1,3,5,7,9,12,19,21]

for num in numbers:
    if (num%3 == 0):
        print(num)


sum = 0
for nums in numbers:
    sum = sum + nums
print('sum: ', sum)


for numss in numbers:
    (numss%2 == 1)
    print(numss ** 2)

cities = ['istanbul','antalya','ankara','izmir','rize']

for city in cities:
    if(len(city)>=5):
        print(city)

products = [
    {'name':'samsung S6', 'price':'3000'},
    {'name':'samsung S7', 'price':'4000'},
    {'name':'samsung S8', 'price':'5000'},
    {'name':'samsung S9', 'price':'6000'},
    {'name':'samsung S10', 'price':'7000'}
]

sums = 0 
for product in products:
    prices = int(product['price'])
    sums = sums + prices
    print(sums)


for product in products:
    if (int(product['price']) <= 5000):
        print(product['name'])