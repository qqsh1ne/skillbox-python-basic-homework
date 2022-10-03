wife_called = 0
hours_count = 0
working_hours = 8
tasks_done = 0
print('Начался ' + str(working_hours) + '-часовой рабочий день')
while hours_count <= working_hours:
    hours_count += 1
    print(str(hours_count) + "-й час")
    tasks_done += int(input("Сколько задач решит Максим? "))
    wife_called += int(input("Звонит жена. Взять трубку? (1-да, 0-нет): "))
    if hours_count == 8:
        print("Рабочий день закончился. Всего выполнено задач:", tasks_done)
        if wife_called > 0:
            print("Нужно зайти в магазин.")
        break
print()