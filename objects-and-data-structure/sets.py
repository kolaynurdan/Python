fruits = {'orange', 'apple', 'banana'}

for x in fruits:
    print(x)

fruits.add('strawberry')
fruits.update(['mango', 'grape'])

print(fruits)

fruits.remove('mango')
fruits.discard('strawberry')

print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)