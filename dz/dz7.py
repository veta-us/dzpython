import random

n = int(input())

spisok = []

for i in range(n+1):
    spisok.append(random.randint(n * -1, n + 1))

print('Введите позицию')

pos = int(input())


