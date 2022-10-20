#Напишите программу, которая будет преобразовывать 
#десятичное число в двоичное.

#_____вариант решения с делением остатка_____ 

#mynumber = int(input()) 
#binary = '' 
#while mynumber > 0:
#    binary = str(mynumber % 2) + binary
#    mynumber = mynumber // 2

#print(binary)


#_____вариант решения с использованием функции bin____
mynumber2 = int(input())
bin_number = bin(mynumber2) 
print(bin_number)
