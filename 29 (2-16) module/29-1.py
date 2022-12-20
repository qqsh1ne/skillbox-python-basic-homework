from typing import Callable
import functools


def check_permission(user: str) -> Callable:
    """
    Декоратор проверки доступа

    :param user: Уровень доступа

    :return: Декоратор функции, которую необходимо выполнить
    """
    def permission(func: Callable) -> Callable:
        """
        Декоратор функции, которая выполнится,
        только если у пользователя есть необходимый доступ

        :param func: Декорируемая функция
        :return: Декорируемая функция с проверенным уровнем доступа и,
                 в зависимости от этого, выполненная или нет
        """
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            return func

        return wrapped

    return permission


user_permissions = ['admin']


@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


delete_site()
add_comment()
