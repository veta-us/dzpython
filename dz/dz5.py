# Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.


n = int(input())
 
factorial = 1
answer = []
i = 1 
for i in range(1, n+1):
    factorial *= i
    answer.append(factorial)
    
    
print(answer)


