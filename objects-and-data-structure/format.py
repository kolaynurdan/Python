name = 'Nurdan'
surname = 'Kolay'
age = 30

print('My name is {} {}'.format(name, surname))
print('My name is {1} {0}'.format(name, surname))
print("My name is {s} {n} and I am ".format(n=name, s=surname))
print("My name is {} {} and I am {}.".format(name, surname, age))

result = 200 / 700
print('the result is {r:1.3}'.format(r=result)) #3 number signs which number after comma.
print('the result is {r:1.4}'.format(r=result)) #3 number signs which number after comma.

print(f"My name is {name} {surname} and I am {age}.") #we defined first.