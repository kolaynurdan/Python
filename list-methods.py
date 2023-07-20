numbers =[1,10,5,16,4,9,10]
letters =['a','g','s','b','y','a','s']

val = min(numbers)
print(val)

val = max(numbers)
print(val)

val = min(letters)
print(val)

val = max(letters)
print(val)

val = numbers[3:6]
print(val)

val = letters[3:6]
print(val)

numbers[4] = 40
print(numbers)

numbers.append('49') #string
print(numbers)

numbers.append(49) #int
print(numbers)

numbers.append(59) #int
print(numbers)

numbers.insert(3,78) #index 3, add int value 78 
print(numbers)

numbers.insert(-1,52)
print(numbers)

numbers.pop() #last item in list
print(numbers)

numbers.pop(0) #first item in list
print(numbers)

numbers.remove(9)
print(numbers)

letters.sort() #sorting a-z
print(letters)

numbers.sort(key=int) 
print(numbers)

numbers.reverse()
print(numbers)

letters.reverse()
print(letters)

print(numbers.count(10))
print(numbers.count('a'))

numbers.clear()
print(numbers)