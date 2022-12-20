from typing import Callable

app = dict()


def callback(key: str) -> Callable:

    def wrapper(func: Callable) -> Callable:
        app[key] = func
        return func

    return wrapper


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
