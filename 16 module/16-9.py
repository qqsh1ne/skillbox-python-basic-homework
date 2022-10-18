friends = int(input('Кол-во друзей: '))
receipts = int(input('Долговых расписок: '))
friends_list = []

for _ in range(friends):
    friends_list.append(0)

for number in range(receipts):
    print(f'\n{number + 1} расписка')
    debtor = int(input('Кому: '))
    lender = int(input('От кого: '))
    money = int(input('Сколько: '))
    friends_list[lender - 1] += money
    friends_list[debtor - 1] -= money

print('\nБаланс друзей:')
for index in range(friends):
    print(f'{index + 1}: {friends_list[index]}')