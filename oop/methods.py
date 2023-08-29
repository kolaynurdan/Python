class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self, yrcp=1):
        self.yrcp = yrcp

    #Methods
    def y_calculate(self):
        return 2*self.pi+self.yrcp
    
    def a_calculate(self):
        return (self.pi)*(self.yrcp**2)
    
c1 = Circle()
c2 = Circle(5)


print(f'c1: {c1.y_calculate()} c2: {c1.a_calculate()}')
print(f'c2: {c2.y_calculate()} c2: {c2.a_calculate()}')