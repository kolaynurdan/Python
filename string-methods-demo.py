website = "http://www.nurdankolay.com"
course = "Python course: Python Programming"

#1- ' Hello World '- delete the spaces at the beginning and end of the list.

result = ' Hello World '
result = result.strip()
print(result)

#just left space
result2 = result.lstrip()
print(result2)

#just right space
result3 = result.rstrip()
print(result3)


resultt = website.lstrip('/:pth')
print(resultt)

# 2- 'www.nurdankolay.com' delete characters except nurdankolay.

s = 'www.nurdankolay.com'.strip('w.com')
print(s)

# 3- 'course' make all characters in the string small.

res = course.lower()
#upper method
res = course.upper()
