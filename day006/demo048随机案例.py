import random

peoples = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6', 'demo7', 'demo8']
rooms = [[], [], []]
i = 0
while i < len(peoples):
    randint = random.randint(0, 2)
    rooms[randint].append(peoples[i])
    i += 1

print("==================================================")
print(rooms)
