def get_vibrations(start, end):
    count = 0
    while start > end:
        start -= (start * DECREMENT / 100)
        count += 1
    return count


DECREMENT = 8.4
start_ampl = float(input('Введите начальную амплитуду (больше нуля и больше амплитуды остановки): '))
end_ampl = float(input('Введите амплитуду остановки (больше нуля): '))
while (start_ampl < 0) or (end_ampl < 0) or (start_ampl <= end_ampl):
    print('Начальная амплитуда и амплитуда остановки должны быть больше нуля.\n'
          'Так же начальная амплитуда должна быть больше амплитуды остановки.')
    start_ampl = float(input('Введите начальную амплитуду: '))
    end_ampl = float(input('Введите амплитуду остановки: '))
print(f'Маятник считается остановившимся через {get_vibrations(start_ampl, end_ampl)} колебаний.')
