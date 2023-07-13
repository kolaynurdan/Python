#String Methods

message = 'Hello There. I am Nurdan'
message = message.upper() #write uppercase each letter
print(message)
message = message.lower() #write lowercase each letter 
print(message)
message = message.title() #just first letter of words upper
print(message)
message = message.capitalize() #The first letter of the first word is capitalized.
print(message)
message = message.strip() #removes leading and trailing spaces.
print(message)
message = message.split() #writes each word separately.
print(message)
print(message[0]) #first word
#message = message.split('.') #writes to separate with '.'
print(message)

message2 = 'I worked so hard today.'
message2 = message2.split() #we want to separate list
print(message2)
message2 = '*'.join(message2) #we want to join list 
print(message2)

