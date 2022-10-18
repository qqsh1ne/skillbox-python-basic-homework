def is_palindrome(numbers):
    reverse_list = []
    for i_number in range(len(numbers) - 1, -1, -1):
        reverse_list.append(numbers[i_number])
    if numbers == reverse_list:
        return True
    else:
        return False


numbers_count = int(input('Кол-во чисел: '))
numbers, new_numbers, answer = [], [], []

for _ in range(numbers_count):
    numbers.append(int(input('Число: ')))

for i_number in range(0, len(numbers)):
    for j_element in range(i_number, len(numbers)):
        new_numbers.append(numbers[j_element])
    if is_palindrome(new_numbers):
        for i_answer in range(0, i_number):
            answer.append(numbers[i_answer])
        answer.reverse()
        break
    new_numbers = []

print('Последовательность:', numbers)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)
