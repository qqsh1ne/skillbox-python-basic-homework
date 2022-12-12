def evaluate_problem(op_1, op_2, operand):
    if op_2 == 0:
        raise ZeroDivisionError('Деление на ноль!!!')
    if operand == '+':
        return op_1 + op_2
    if operand == '-':
        return op_1 - op_2
    if operand == '*':
        return op_1 * op_2
    if operand == '/':
        return op_1 / op_2


def evaluate_all(line):
    global all_sum
    line = line.replace('\n', '')
    data = line.split()
    operand = data[1]
    try:
        if len(operand) != 1:
            raise TypeError
        op_1 = int(data[0])
        op_2 = int(data[2])
        all_sum += evaluate_problem(op_1, op_2, operand)
    except (TypeError, SyntaxError, ValueError, ZeroDivisionError):
        print(f'Обнаружена ошибка в строке: {line}')
        answer = input('Хотите исправить? ')
        if answer.lower() == 'да':
            evaluate_all(input('Введите исправленную строку: '))


all_sum = 0

with open('calc.txt', 'r', encoding='utf-8') as f_calc:
    for line in f_calc:
        evaluate_all(line)

print(all_sum)