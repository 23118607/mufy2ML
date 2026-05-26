import random
adj = ["Brave", "Humble", "Furious" ]
animal = ["Lion", "Otter", "Penguin"]

randname = (random.choice(adj) + " " + random.choice(animal))

randnum = (random.randint(1, 100))

print("What is your name? ")
name = input()
print(name + ", your codename is:" + randname)
print(f"Your lucky number is: {randnum}")