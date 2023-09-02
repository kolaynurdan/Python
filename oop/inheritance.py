#Inheritance

#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person) 

#Animal => Dog(Animal), Cat(Animal)
class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('i am eating')

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        print('Student Created')
    #overriding
    def who_am_i(self):
        print('I am a student')

p1 = Person('Ali','Yilmaz')
s1 = Student('Nurdan','Kolay')

print(p1.firstName, p1.lastName)
print(s1.firstName, s1.lastName)

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()