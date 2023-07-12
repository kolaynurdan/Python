name = 'Nurdan'
surname = 'Kolay'
age = 30
"""
greeting= 'My name is '+ name +' '+'surname '+surname+' and\nI am '+str(age)
print(greeting)
print(greeting[0])
print(greeting[3])
print(len(greeting))
print(greeting[-1]) #last letter
print(greeting[3:7]) #specified range
print(greeting[3:]) #starting within index 3 and going up to
print(greeting[:15]) #starting within index beginning and go up to index 15
print(greeting[2:40:2]) #Increase by two starting from 2 and going up to 40
"""

website = 'https://www.nurdankolay.com'
course = "Python training from scratch"

#1- How many characters are in the 'course' string?
result = len (course)
print(result)

#2- Get the www characters from the 'website' variable
result = website[8:11]
print(result)

#3- Get the com characters from the 'website' variable
#1.way
result = website[24:27]
print(result)

#2.way
length = len(website)
result = website[length-3:length]
print(result)

#4- Get the first 15 and last 15 characters from 'course'.
resultFirst15 = course[0:15]
print(resultFirst15)
resultLast15 = course[-15:]
print(resultLast15)

#5- Reverse the characters in the course variable.
result = course[::-1]
print(result)

s = '12345' * 5
print(s[::5]) #we write 1 at per 5 charachters.

#6- Print the expression to the screen with the given variables.
#My name is Nurdan. I am 30 years old. And I am a Computer Engineer
name, age, job = 'Nurdan', 30, 'Computer Engineer'
result = 'My name is ' + name + 'I am '+str(age)+'.'+' years old. And I am a '+job+'.'
result = 'My name is {}. I am {}. And I am a {}'.format(name, age, job)
result = f"My name is {name}. I am {age}. And I am a {job}"
print(result)

#7- Let's swap w and W in the hello world expression.
s = 'Hello world'

#1.way
s = s[0:6] + 'W' + s[-4:]
print(s)

#2.way
s.replace('w','W')
print(s)

#8- Print 'abc' expression side by side 3 times.
result = 'abc '*3
print(result)