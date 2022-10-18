skates_size = []
foot_size = []
count = 0

for i in range(int(input('Кол-во коньков: '))):
    skates_size.append(int(input('Размер ' + str(i + 1) + ' пары: ')))

for i in range(int(input('\nКол-во людей: '))):
    foot_size.append(int(input('Размер ноги ' + str(i + 1) + ' человека: ')))

skates_size.sort()
foot_size.sort()

for i in foot_size:
    for j in range(len(skates_size)):
        if skates_size[j] >= i:
            skates_size.remove(skates_size[j])
            count += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
