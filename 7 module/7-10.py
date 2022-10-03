cards_amount = int(input('Введите количество карточек: '))
left_cards_sum, cards_number_sum = 0, 0
for card_number in range(1, cards_amount + 1):
    cards_number_sum += card_number

for card_number in range(1, cards_amount):
    left_cards_sum += int(input('Введите номер карты: '))
print('Потерянная карточка под номером', (cards_number_sum - left_cards_sum))
