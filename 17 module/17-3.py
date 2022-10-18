import random


players = 20
start = 5
end = 10
fst_team = [round(random.uniform(start, end), 2) for _ in range(players)]
sec_team = [round(random.uniform(start, end), 2) for _ in range(players)]

print('Первая команда:', fst_team)
print('Вторая команда:', sec_team)

print('Победители тура:', [(fst_team[i] if fst_team[i] > sec_team[i] else sec_team[i]) for i in range(players)])
