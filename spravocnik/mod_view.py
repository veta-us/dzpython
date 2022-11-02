def show_menu() -> int:
    print("\n Выберите действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить нового абонента\n"
        "5. Сохранить справочник в текстовом формате\n"
        "6. Выход из справочника")
    choice = int(input())
    return choice

def result(data: list):
    for elements in data:
        a = ''
        for v, k in elements.items():
            a += f'{v}: {k}\n'  
        print(a)

def search_name() -> str:
    return input("ВВедите фамилию: ")

def search_number() -> str:
    return input("ВВедите номер телефона: ")

def new_user() -> str:
    first_name = input("ВВедите имя: ")
    second_name = input("ВВедите фамилию: ") 
    phone_nmber = input("ВВедите номер: ") 
    comment = input("ВВедите комментарий: ") 
    return f'{first_name},{second_name},{phone_nmber},{comment}'

def get_file_name() -> str:
    return input("Введите название файла, чтобы сохранить:  ")