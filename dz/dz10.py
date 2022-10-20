#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


#решение последовательностb Фибоначчи
print('Введите число:');
number = int(input())

fib1 = fib2 = 1
 
print(fib1, fib2, end=' ')
 
for i in range(2, number):
   fib1, fib2 = fib2, fib1 + fib2
   print(fib2, end=' ') 

