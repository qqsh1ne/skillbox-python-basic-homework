import time
from collections.abc import Callable
from datetime import datetime
from typing import Any


def timer(cls: Callable, func: Callable, date_format: str) -> Callable:
    """
    Декоратор методов. Используется для вывода даты запуска функции и времени ее работы

    :param cls: Класс, методы которого декорируются

    :param func: Декорируемый метод

    :param date_format: Формат, в котором необходимо логировать метод

    :return: Декорированная функция
    """
    def wrapped(*args, **kwargs) -> Any:
        format_str = date_format
        for symbol in format_str:
            if symbol.isalpha():
                format_str = format_str.replace(symbol, '%' + symbol)
        start = time.time()
        print(f"Запуск '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format_str)}")
        result = func(*args, **kwargs)
        print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(time.time() - start, 3)} сек.")
        return result

    return wrapped


def log_methods(date_format: str) -> Callable:
    """
    Декоратор класса. Логирует вызовы его методов в переданном формате

    :param date_format: Формат даты, в котором нужно логировать метод
    """
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
