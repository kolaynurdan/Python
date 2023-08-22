def tBb(num):
    tb=[]

    for i in range(2, num):
        if (num % i == 0):
            tb.append(i)
    
    return tb

print(tBb(20))