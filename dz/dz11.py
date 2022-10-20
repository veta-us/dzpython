#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

spisok = [2, 3, 4, 5, 6, 8]
length = len(spisok)
length2 = length//2
answer = []
for i in range(length2):
    answer.append(spisok[i] * spisok[-i -1])
    if length % 2 == 1:
        answer.append(spisok[length2]**2)

print(answer)

