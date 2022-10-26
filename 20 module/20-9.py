games_quantity = int(input('Сколько записей вносятся в протокол? '))

games = []

print('Записи (результат и имя):')

for i_game in range(1, games_quantity + 1):
    score, name = input(f'{i_game}-я запись: ').split()
    score = int(score)

    is_continued = False
    for i, i_data in enumerate(games):
        if name == i_data[1]:
            if score > i_data[0]:
                games[i] = (score, name)
                games.sort(reverse=True, key=lambda player_data: player_data[0])
            is_continued = True
            continue
    if is_continued:
        continue

    if len(games) < 3:
        games.append((score, name))
    else:
        min_score = games[2][0]
        if score > min_score:
            games[2] = (score, name)
    games.sort(reverse=True, key=lambda player_data: player_data[0])


print('Итоги соревнований:')
print(f'1-е место. {games[0][1]} ({games[0][0]})\n2-е место. {games[1][1]} ({games[1][0]})\n3-е место. {games[2][1]} ({games[2][0]})')
