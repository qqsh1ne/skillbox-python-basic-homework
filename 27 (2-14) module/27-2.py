import time
import functools
from typing import Callable, Any


def freeze(func: Callable) -> Any:
    """
    Декоратор, замедляющий работу функции на 3 секунды

    :param func: Декорируемая функция
    """

    @functools.wraps(func)
    def wrapped_func():
        time.sleep(3)
        func()

    return wrapped_func


@freeze
def test():
    print('В стадии разработки....')


test()