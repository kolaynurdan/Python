website = "http://www.nurdankolay.com"
course = "Python course: Python Programming from Scratch bla bla"

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
variable3 = website.find('com',0,26) #range
print(variable3)
variable4 = course.find('Python')
print(variable4)
variable5 = course.rfind('Python')
print(variable5)

#7- 'course' is alpha or is digit?
result5 = course.isalpha()
print(result5) #there is a sign character. bool answer is false.
variable6 = 'hello'.isalpha()
print(variable6)
result6 = course.isdigit()
print(result6)
result7 = '123'.isdigit()
print(result7)

#8- put left and right '*' char 'contents' expression.

result4 = 'Contents'.center(50,'*')
print(result4)
result8 = 'Contents'.ljust(50,'*')
print(result8)
result9 = 'Contents'.rjust(50,'*')
print(result9)

#9- we replace all of spaces with '-' in 'course'.

result10 = course.replace(' ','-')
print(result10)
result11 = course.replace(' ','-',5)
print(result11)
result12 = course.replace(' ','')
print(result12)

#10- we want to change 'Hello World' to 'Hello There'
result13 = 'Hello World'.replace('World','There')
print(result13)

#11- 'course' list split spaces.
result14 = course.split(' ')
print(result14)