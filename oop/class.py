#class

class Person:
    pass
    #attributes 
    #constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print("init methods are worked.")
    #methods

#object instance
p1 = Person('ali',1990)
p2 = Person('hasan',1993)

print(f'name: {p1.name} year: {p1.year}')
print(f'name: {p2.name} year: {p2.year}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))