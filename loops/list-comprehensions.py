for x in range(10):
    print(x)

numbers = [x for x in range(10)]
print(numbers)

numberss=[]
for x in range(10):
    numberss.append(x)
print(numberss)

for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]

numbers23 = [x*x for x in range(10) if x % 3 ==0]
print(numbers23)

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myString)

myListt = [letter for letter in myString]
print(myListt)

years = [1983, 1999, 2008, 1956, 1986]
ages = [2019-year for year in years]
print(ages)

resultsss = [x if x%2 ==0 else 'T' for x in range(1,10)]
print(resultsss)


ress= []

for x in range(3):
    for y in range(3):
        ress.append((x,y))
print(ress)

numbr = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbr)