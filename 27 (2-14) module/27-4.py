from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор. Считают количество вызовов и выводит в консоль

    :param func: Декорируемая функция
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызывалась {wrapped_func.count} раз')
        return result

    wrapped_func.count = 0
    return wrapped_func


@counter
def test() -> None:
    print('В разработке....')


test()
test()
test()
test()
test()
test()
