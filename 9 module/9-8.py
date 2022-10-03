total_length = int(input('Введите общую длину колонтитула: '))
marks = int(input('Введите количество восклицательных знаков: '))
print(('~' * ((total_length - marks) // 2)) + ('!' * marks) + ('~' * ((total_length - marks) // 2)))