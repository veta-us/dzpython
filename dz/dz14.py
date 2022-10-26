#Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

#вариант, если текст уже напишу я сама 
#text = 'тут я пишу суперсложный абвтекст, где алфавит и первые три буквы алфавита абвгд' 

print('Введите длинный текст: ')
text = input(())
print(text)
def delete_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(my_text)

text = delete_words(text)
print('текст после удаления слов с "абв":   ', text)
