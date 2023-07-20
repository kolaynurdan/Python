names = ['Nurdan','Nuray','Ayse','Nuri']
years = [1993,1990,1964,1662]

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
