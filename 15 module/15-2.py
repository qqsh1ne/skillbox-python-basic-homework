players = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day_players = []

for i_players in range(0, len(players), 2):
    first_day_players.append(players[i_players])

print('Первый день:', first_day_players)