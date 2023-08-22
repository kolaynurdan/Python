#1

def printedExpression(words,count):
    print(words * count)

printedExpression('Hello\n',10)

#2

def turnToList(*params):
    list = []

    for param in params:
        list.append(param)

    return list

result = turnToList(10,20,30,'Hello')

print(result)

#3

def primeNumberFind(num1, num2):
    for num in range(num1,num2+1):
        if num > 1:
            for i in range(2,num):
                if (num % i == 0):
                    break
            else:
                print(num)

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))

primeNumberFind(num1,num2)

#4

def tBb(num):
    tb=[]

    for i in range(2, num):
        if (num % i == 0):
            tb.append(i)
    
    return tb

print(tBb(20))