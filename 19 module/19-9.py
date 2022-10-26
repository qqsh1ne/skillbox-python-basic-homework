pedigree_data, levels = {}, {}

for i_pare in range(1, int(input('Введите количество человек: '))):
    pare = input(f'{i_pare} пара: ').split()
    child_name, parent_name = pare[0], pare[1]
    pedigree_data[child_name] = parent_name
    levels[child_name], levels[parent_name] = 0, 0

for child_name in pedigree_data:
    temp_child_name = child_name
    while temp_child_name in pedigree_data:
        temp_child_name = pedigree_data[temp_child_name]
        levels[child_name] += 1

print('\n“Высота” каждого члена семьи:')
for i_pare in sorted(levels):
    print(i_pare, levels[i_pare])