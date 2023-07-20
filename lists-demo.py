#1- create a list in "Bmw, Hundai, Fiat, Tofas, " members.
cars =['Bmw','Hundai','Fiat','Tofas']
print(cars)
#2- How many members in this list?
result = len(cars)
print(result)
#3- first member and last member this list
result = cars[0]
print(result)
result = cars[-1]
print(result)
#4- you can change 'Hundai' to 'Mazda'
cars[-1] = 'Mazda'
print(cars)
#5- is 'bmw' member in this list?
result = 'Bmw' in cars
print(result)
#6- list in -2 index
result = cars[-2]
print(result)
#7- first 3 elements of the list
result = cars[0:3]
#result = cars[:3]
print(result)
#8- add toyota and peugeot instead of last 2 items of list
cars[-2:] = ['Toyota','Peugeot']
print(cars)
#9- Add 'Nissan' and 'Audi'
result = cars + ['Nissan', 'Audi']
print(result)
#10- Delete last item in this list
del cars[-1]
result = cars
print(result)
#11- print the list elements in reverse.
result = cars[::-1]
print(result)
#12- store below data in list
   #studentA : Nurdan Kolay 1993, (70,60,70)
   #studentB : Ayse Fatma 1995, (90,65,75)
   #studentC : Fatma Ayse 2010, (50,40,90)
studentA = ['Nurdan','Kolay', 1993, [70,60,70]]
studentB = ['Ayse','Fatma', 1995, [90,65,75]]
studentC = ['Fatma','Ayse', 2010, [50,40,90]]

#13- print list members
print(studentA[0])
print(studentB[1])
print(studentC[3])
print(studentC[3][1])

result = f"{studentA[0]} {studentA[1]} adinda {2019-studentA[2]} yasinda {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)