list_length = int(input('Введите количество чисел в списке: '))
numbers = []
for _ in range(list_length):
    numbers.append(int(input('Введите число: ')))

for _ in numbers:
    for j_number in range(list_length - 1):
        if numbers[j_number] > numbers[j_number + 1]:
            numbers[j_number], numbers[j_number + 1] = numbers[j_number + 1], numbers[j_number]

print(numbers)
