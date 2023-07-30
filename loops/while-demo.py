numbers = [1,3,5,7,9,12,19,21]

i = 0
while(i<len(numbers)):
    print(numbers[i])
    i += 1 

starting = int(input('Start: '))
ending = int(input('End: '))

i = starting
while (i<ending):
    i += 1 
    if i%2 == 0:
        print(i)

i = 100 

while i > 0:
    print(i)
    i -= 1

numbers = []

i = 0

while i < 5:
    num = int(input('Number: '))
    numbers.append(num)
    i+=1
print(numbers)

products = []

count = int(input('How many products in list?: '))
i = 0

while(i<count):
    name = input('Product name: ')
    price = input('Product price: ')
    products.append(
        {
            'name': name,
            'price': price
        }
    )
    i+=1

for product in products:
    print(f'Product Name: {product["name"]} Product Price: {product["price"]}')