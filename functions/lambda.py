def square(num): return num ** 2

numbers = [1,3,5,9,10,12,14]

result = list(map(lambda num: num ** 2, numbers))

result = list(map(square, numbers))

for item in map(square,numbers):
    print(item)

print(result)

check_even = lambda num: num%2 == 0

result = list(filter(check_even, numbers))

print(result)