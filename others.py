# Identity Operator : is

x = y = [1,2,3]
z = [1,2,3]

print(x == y)
print(x == z)

print(x is y) #True
print(x is z) #False - beacause of different reference

h = [1,2,3]
k = [2,4]
k.reverse()

del h[2]
k[1] = 1

print(h == k)
print(h is k)
print(h is not k)

#Membership Operator: in

x = ['apple','banana']

print('banana' in x)

name = 'Nurdan'
print('a' in name)
print('n' not in name)