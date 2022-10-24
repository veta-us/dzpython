#Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.


rint ('ввоедите числа один за одним через enter и введите х - знак стоп')

sequence = []

user_input = True

while user_input:
    i = input()
    if i == 'x':
        user_input = False
    else:
        sequence.append(i)

print (list(set(sequence)))