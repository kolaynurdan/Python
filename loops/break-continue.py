name = 'Nurdan Kolay'

for letter in name:
    if letter == 'a':
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x+=1

x = 1
result = 0

while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x
print(f'Sum: {result}')