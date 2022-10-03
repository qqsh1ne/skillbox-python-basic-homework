end_number = int(input('Введите число, до которого хотите возводить степень: '))
current_number = 1

while current_number <= end_number:
    print(str(current_number) + ' в кубе равно ' + str(current_number ** 3))
    current_number += 1
