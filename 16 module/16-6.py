first_list_length = 3
second_list_length = 7
first_list = []
second_list = []

for i_number in range(first_list_length):
    first_list.append(int(input(f'Введите {i_number + 1}-е число для первого списка: ')))

for i_number in range(second_list_length):
    second_list.append(int(input(f'Введите {i_number + 1}-е число для второго списка: ')))

unique_numbers = []

first_list.extend(second_list)

for _ in range(len(first_list)):
    for i in first_list:
        if first_list.count(i) > 1:
            first_list.remove(i)

print(first_list)
