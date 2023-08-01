list = [1,2,3]

for item in list:
    print(item)


for item in range(10):
    print(item)

for item in range(2,10):
    print(item)

for item in range(5,100,10):
    print(item)


index = 0 
greeting = 'Hello There'

for letter in greeting:
    print(f'letter: {letter} index: {index}')
    index += 1

#enumerate

greeting2 = 'Hello'
for index,letter in enumerate(greeting2):
    print(f'index: {index} letter: {letter}')


for item in enumerate(greeting2):
    print(item)

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

for item in zip(list1,list2):
    print(item)