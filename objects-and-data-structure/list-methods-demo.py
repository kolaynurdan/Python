names = ['Nurdan','Nuray','Ayse','Nuri']
years = [1993,1990,1964,1962]

#1- Add 'Ummuhan' item in names list.
names.append('Ummuhan')
print(names)

#2- Add 'Emine' item first of names list.
names.insert(0, 'Emine')
print(names)

#3- Delete 'Nurdan' item at names list.
names.remove('Nurdan')
print(names)
#names.pop()
#print(names)

#4- find 'Nuri' item in index?
index = names.index('Nuri')
#names.pop(index)
print(index)

#5- is 'Ayse' in name list?
result = 'Ayse' in names
print(result)

#6- reverse names list.
names.reverse()
print(names)

#7- 'names'sort the list elements alphabetically.
names.sort()
print(names)

#8- 'names'sort the list elements numerically.
years.sort()
print(years)

#9- turn str = "Chevrolet, Dacia" this char series into list.
str = "Chevrolet, Dacia"
result = str.split(',')
print(result)

#10- 'years' char series min and max values?
min = min(years)
print(min)
max = max(years)
print(max)

#11- how many '1993' in 'years' list?
result = years.count(1993)
print(result)

#12- clean 'years' list.
years.clear()
print(years)

#13- Keep 3 brands that you will receive from the user in a list.
brands = []
brand = input('brand:')
brands.append(brand)
print(brands)

brand = input('brand:')
brands.append(brand)
print(brands)

brand = input('brand:')
brands.append(brand)
print(brands)