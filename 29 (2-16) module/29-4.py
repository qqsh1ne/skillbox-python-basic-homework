import functools


def singleton(cls):
    """
    Декоратор класса. Превращает класс в синглтон, т.е., он может иметь только одну сущность

    :param cls: Декорируемый класс, который необходимо превратить в синглтон
    """
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)