def get_winners(players, min_score):
    winners = []
    current_number = 0
    for player in players:
        player_data = player.split()
        if player_data[2] > min_score:
            current_number += 1
            winners.append(player_data)
    winners.sort(key=lambda x: x[2], reverse=True)
    return winners


def get_second_tour_members(winners):
    result = str(len(winners)) + '\n'
    for winner in winners:
        result += f'{len(winners)}) {winner[1][0]}. {winner[0]} {winner[2]}\n'
    passed = open('second_tour.txt', 'w', encoding='utf8')
    passed.write(result)
    passed.close()


results = open('first_tour.txt', 'r', encoding='utf8')
lines = list(results.readlines())
results.close()

min_score = lines[0][:-1]
players = []

for line in lines[1:]:
    players.append(line[:-1])

get_second_tour_members(get_winners(players, min_score))
