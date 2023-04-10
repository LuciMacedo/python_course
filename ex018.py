import random

n1 = str(input('Name1: '))
n2 = str(input('name2: '))
n3 = str(input('name3: '))
n4 = str(input('name4: '))
lista = [n1, n2, n3, n4]
chosen = random.choice(lista)

print(chosen)