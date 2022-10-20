#Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка,
#стоящих на нечётной позиции.


spisok = [2, 3, 5, 9, 3]
print(spisok)
summa = 0

for i in range(len(spisok)):
    if i % 2 == 1:
        summa += spisok[i]

print(summa)




    


