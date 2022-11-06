from mod_view import (show_menu, result, search_name, search_number, new_user, get_file_name)

from model import write_txt, write_csv, read_csv, find_by_name, find_by_number, add_user

def work_phonebook():
    choice = show_menu()
    phone_book = read_csv('my_phonebook.csv')

while (choice != 6):
    if choice == 1:
        result(phone_book)
    elif choice == 2:
        name = search_name()
        print(find_by_name(phone_book, name))
    elif choice == 3:
        number = search_number()
        print(find_by_number(phone_book, name))
    elif choice == 4:
        user_data = new_user
        add_user(phone_book, user_data)
        write_csv('my_phonebook.csv', phone_book)
    elif choice == 5:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
        choice = show_menu()

        

