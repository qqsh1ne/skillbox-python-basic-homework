import datetime
import functools
from typing import Callable, Any


def logging(func: Callable) -> Any:
    """
    Декоратор логирования ошибок рантайма функций. Ошибки записываются в function_errors.log

    :param func: Декорируемая функция
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        with open("function_errors.log", "a") as log_file:
            try:
                print(f'Название функции: {func.__name__}\nОписание функции: {func.__doc__}')
                return func(*args, **kwargs)
            except Exception as e:
                log_file.write(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
                               + ' ' + func.__name__ + " "
                               + type(e).__name__ + '\n')
    return wrapped_func


@logging
def print_list(lst: list) -> None:
    """
    Функция печати 5 элементов списка

    :param lst: Список
    """
    for i in range(5):
        print(lst[i])


@logging
def convert_to_int(string: str) -> int:
    """
    Функция преобразования значения в integer

    :param string: Значение
    :return: int
    """
    return int(string)


with open('function_errors.log', 'w') as log:
    log.close()

my_list = [i for i in range(2)]
print_list(my_list)
number = convert_to_int("Не число")
