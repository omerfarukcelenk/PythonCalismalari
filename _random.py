import random   

# result = dir(random)
# result = help(random)

result = random.random() * 100 # 0.0 ile 1.0 arası sayaı üretir
result = int(random.uniform(1,20))
result = random.randint(100,200)
greeting = "Hello There"
names = ["Ali","Ömer", "mehret", "Muzoger"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)

result = random.sample(liste, 3)
result = random.sample(names,2)
print(result)