number = int(input('Введите число: '))
odd_numbers =[]
for odd_number in range(1, number + 1, 2):
    odd_numbers.append(odd_number)
print(odd_numbers)