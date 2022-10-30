
#программа берет список, и возвращает новый список только с положительными элеменатми первого списка
spisok = [65, -6, 565, 0, 4, 1, 54, 0, -3, -56, 87]
newlist = list(filter(lambda x: x > 0, spisok))  #lambda отбирает положительные элементы списка spisok
print(newlist)

#тренировка функции map
#zadacha1
my_spisok = [1, 2, 3, 4, 5, 6, 7, 8]
newlist = list(map(lambda x: x*3 - 4 , my_spisok))
print(newlist) 

#zadacha2, возвести элементы списка в квадрат
def square(number):
    return number ** 2
numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))

#решение вместе с lambda
second_numbers = [1, 2, 3, 4, 5]
second_squared = map(lambda x: x ** 2, second_numbers)
print(list(second_squared))


# Улучшила программу:
# ____Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.____

# .....Вариант ДО.....
# n = int(input())
# factorial = 1
# answer = []
# i = 1 
# for i in range(1, n+1):
#     factorial *= i
#     answer.append(factorial)   
# print(answer)

#......Вариант ПОСЛЕ.....

# n = int(input("ВВедите число N: "))
# spisok = list(range(1, n+1))
# import math
# print(list(map(math.factorial, spisok)))

#использовала List Comprehensions

n = int(input("ВВедите число N: "))
spisok = [x for x in range(1, n+1)]
import math
print(list(map(math.factorial, spisok)))

