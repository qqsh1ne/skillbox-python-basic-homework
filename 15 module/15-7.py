max_weight, max_amount = 200, 200

containers_amount = int(input('Количество контейнеров: '))
containers = []

while containers_amount > max_amount:
    print('Кол-во контейнеров должно быть не больше 200')
    containers_amount = int(input('Количество контейнеров: '))

for i_container in range(containers_amount):
    weight = int(input('Введите вес контейнера:'))
    while weight > max_weight:
        print('Вес контейнера должен быть не больше 200')
        weight = int(input('Введите вес контейнера:'))
    containers.append(weight)

new_container_weight = int(input('Введите вес нового контейнера: '))

i_container = 0
while new_container_weight <= containers[i_container]:
    i_container += 1
    if i_container == len(containers):
        break

print(i_container + 1)
