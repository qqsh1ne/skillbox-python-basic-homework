from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор для вывода 'Как дела?'

    :param func: Декорируемая функция
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как дела?')
        print('А у меня не очень!')
        return func(*args, **kwargs)
    return wrapped_func


@how_are_you
def say_hello(name: str) -> str:
    return f'Hello, {name}!'


@how_are_you
def say_goodbye(name: str) -> str:
    return f'Goodbye, {name}!'


my_func = say_goodbye('Пудж')
print(my_func, '\n')
func_hello = say_hello('Пудж')
print(func_hello)