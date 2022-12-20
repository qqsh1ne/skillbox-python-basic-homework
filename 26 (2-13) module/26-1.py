class Squares:
    """
    Класс-итератор для генерации последовательности из квадратов чисел

    Args:
        limit - максимальное число, до которого надо возвращать квадраты

    Attributes:
        __limit - максимальное число, до которого надо возвращать квадраты
        __current_element - текущий элемент
        __counter - счетчик сгенерированных чисел
    """
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__current_element = 0
        self.__counter = 0

    def __iter__(self):
        self.__current_element = 0
        self.__counter = 0
        return self

    def __next__(self) -> int:
        self.__counter += 1
        if self.__limit <= 0 or self.__counter > self.__limit:
            raise StopIteration
        self.__current_element += 1
        return self.__current_element ** 2


def square(nums: int):
    """
    Возводит в квадрат числа до указанного
    :param nums:
    :return:
    """
    for num in range(1, nums + 1):
        yield num ** 2


max_number = int(input('Введите число от 1 до N: '))
squares = Squares(max_number)
print('\nКласс-итератор')
for squared_number in squares:
    print(squared_number, end=' ')

print('\n\nВывод функция генератор')
for squared_number in square(max_number):
    print(squared_number, end=' ')

print('\n\nВывод генераторное выражение')
square_gen = (number ** 2 for number in range(1, max_number + 1))
for squared_number in square_gen:
    print(squared_number, end=' ')
