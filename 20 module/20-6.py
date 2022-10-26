origin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Оригинальный список:', origin)
print('Новый список:', [(i_element, origin[i + 1]) for i, i_element in enumerate(origin) if i % 2 == 0])
