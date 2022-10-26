def run_contact_book():
    while True:
        action = input('Введите номер действия:\n1. Добавить контакт\n2. Найти человека\n')
        if action == '1':
            add_contact()
        elif action == '2':
            find_contact()
        else:
            print('Неверный номер действия!')


def add_contact():
    name_data = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if contact_book.get(name_data) is not None:
        print('Такой человек уже есть в контактах.')
        return
    contact_book[name_data] = int(input('Введите номер телефона: '))
    print('Текущий словарь контактов: ', contact_book)


def find_contact():
    surname = input('Введите фамилию для поиска: ').lower()
    found_contacts = [f'{i_name[0]} {i_name[1]} {i_phone_number}'for i_name, i_phone_number in contact_book.items() if surname == i_name[1].lower()]
    if len(found_contacts) == 0:
        print('Такого человека нет в списке контактов!')
    else:
        print(*found_contacts, sep='\n')


contact_book = {}
run_contact_book()
