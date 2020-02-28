import random

f = open('input.txt', 'w')
for x in range(1, 101):
    f.write(str(random.randint(1, 10))+"\n")
