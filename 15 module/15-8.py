shift = int(input('Сдвиг: '))
initial_list = [1, 2, 3, 4, 5]
new_list = []

for i_number in range(len(initial_list)):
    new_list.append(initial_list[i_number - shift])

print('Изначальный список:', initial_list)
print('Сдвинутый список:', new_list)