cells_amount = int(input('Количество клеток: '))
bad_efficiency = []

for i_cells in range(1, cells_amount + 1):
    print(f'Эффективность {i_cells} клетки: ', end='')
    efficiency = int(input())
    if efficiency < i_cells:
        bad_efficiency.append(efficiency)

print('Неподходящие значения: ', bad_efficiency)
