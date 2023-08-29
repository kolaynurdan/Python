#class

class Person:
    pass
    #attributes 
    #constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year
    #methods
    def intro(self):
        print('Hello There. I am '+self.name)

    def calculatedAge(self):
        return 2023 - self.year

#object instance
p1 = Person('ali',1990)
p2 = Person('hasan',1993)



#print(p1)
#print(p2)
#print(type(p1))
#print(type(p2))

p1.intro()
p2.intro()

print(f'name: {p1.name} year: {p1.calculatedAge()}')
print(f'name: {p2.name} year: {p2.calculatedAge()}')