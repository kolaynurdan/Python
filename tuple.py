list = [1,2,3]

tuple = (1, 'iki', 3)

#print(type(list))
#print(type(tuple))

#print(list[2])
#print(tuple[2])

#print(len(tuple))
#print(len(list))

list = ['ali','veli']
tuple = ('damla','yaren','yaren')
names = ('demet','mahmut','damla') + tuple

list[0] = 'ahmet'
#dont change tuple member but you can change list member
#tuple[0] = 'deniz' 

print(list)
print(tuple)

print(tuple.count('yaren'))

print(names)