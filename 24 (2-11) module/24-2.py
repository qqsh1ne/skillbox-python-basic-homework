class Student:

    def __init__(self, full_name: str, group_number: str, progress: tuple):
        self.full_name = full_name
        self.group_number = group_number
        self.progress = progress

    def __str__(self):
        return f'ФИО: {self.full_name} Группа: {self.group_number} Средний балл: {self.get_average()}'

    def get_average(self):
        return round(sum(self.progress) / len(self.progress), 2)


def receiving_data():
    return input('ФИО: '), input('Номер группы: '), tuple(map(int, input('Оценки: ').split()))


STUDENTS_COUNT = 1
print('Введите данные студентов:')
list_student = [Student(*receiving_data()) for _ in range(STUDENTS_COUNT)]
print('Список студентов:')
for student in list_student:
    print(student)
print()

list_student.sort(key=lambda x: x.get_average())
print('Список студентов отсортированный:')
for student in list_student:
    print(student)
