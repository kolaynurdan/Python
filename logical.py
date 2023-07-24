x = 6 

right = 5

cont = 'e'

result = 5 < x < 10 

#and

result = x > 5 and x < 10
result = (right > 0 ) and (cont == 'e')

#or

result = (x > 0 ) and (x % 2 == 0)

#not

result = not(x > 0)

#x, is it 5-10 range even number?

(((x > 5) or (x<10)) and (x%2 == 0))


print(result)