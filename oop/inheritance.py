#Inheritance

#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person) 

#Animal => Dog(Animal), Cat(Animal)
class Person():
    def __init__(self):
        print('Person Created')


class Student(Person):
    pass

p1 = Person()
s1 = Student()