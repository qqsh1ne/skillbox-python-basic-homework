guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

command = ''
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    command = input('Гость пришел или ушел? ').lower()
    if command == 'пора спать':
        break
    guest_name = input('Имя гостя: ')
    if command == 'пришел':
        if len(guests) < 6:
            print(f'Привет, {guest_name}!')
            guests.append(guest_name)
        else:
            print(f'Прости, {guest_name}, но мест нет.')
    elif command == 'ушел':
        guests.remove(guest_name)
        print(f'Пока, {guest_name}!')
    print()

print('Вечеринка закончилась, все легли спать.')