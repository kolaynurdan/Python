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
print(res)
#upper method
res = course.upper()
print(res)
#title method
res = course.title()
print(res)
#4- 'website' how many a characters are in it?

ress = website.count('a')
print(ress)
ress = website.count('www')
print(ress)
ress = website.count('www',0,10) #range[0,10]
print(ress)

#5- 'website' starts with 'www', ends with 'com'
w = website.startswith('www')
print(w) #bool type
w = website.startswith('http')
print(w)
w = website.endswith('com')
print(w)

#6- 'website', '.com' char in it?
variable2 = website.find('.com')
print(variable2) #indexnumber
variable3 = website.find('')
#7- 