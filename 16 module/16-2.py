def bubble_sort(array):
    for _ in array:
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


first_grade_min = 160
first_grade_max = 176
first_grade_step = 2
second_grade_min = 162
second_grade_max = 180
second_grade_step = 3

first_grade = list(range(first_grade_min, first_grade_max + 1, first_grade_step))
second_grade = list(range(second_grade_min, second_grade_max + 1, second_grade_step))

first_grade.extend(second_grade)
print('Отсортированный список учеников:', bubble_sort(first_grade))