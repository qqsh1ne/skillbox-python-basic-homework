print("Введите местоположение коня:")
horse_x, horse_y = float(input()), float(input())
print("Введите местоположение точки на доске:")
point_x, point_y = float(input()), float(input())

horse_x_square, horse_y_square = int(horse_x * 10), int(horse_y * 10)
point_x_square, point_y_square = int(point_x * 10), int(point_y * 10)
print(f'Конь в клетке ({horse_x_square}, {horse_y_square}). Точка в клетке ({point_x_square}, {point_y_square}).')

dx, dy = abs(horse_x_square - point_x_square), abs(horse_y_square - point_y_square)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь НЕ может ходить в эту точку.')