import random

result = dir(random)

result = random.random() #0-1 range
result = random.random()*100
result = random.uniform(1,10)
result = int(random.uniform(10,100))
result = random.randint(1,100)

greeting = 'hello there'
names = ['ali','yagmur','deniz','cenk']
result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)
print(result)