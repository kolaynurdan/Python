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
p1 = Person()
p2 = Person()
print(p1)
print(p2)
print(type(p1))
print(type(p2))