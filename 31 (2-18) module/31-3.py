from typing import List
import requests
import json


def get_starship_info(starship_url: str, file_name: str) -> None:
    """
    Выводит в консоль и записывает в json файл данные о корабле
    :param starship_url: URL адрес корабля, который необходимо обработать
    :param file_name:Имя файла (обязательно формата .json), куда необходимо записать данные о корабле
    """
    starship_data = requests.get(starship_url)
    starship_info = json.loads(starship_data.text)
    result = {
        'ship_name': starship_info['name'],
        'starship_class': starship_info['starship_class'],
        'max_atmosphering_speed': starship_info['max_atmosphering_speed'],
        'pilots': get_pilots(starship_info),
    }
    print(result)
    with open(file_name, 'w') as file:
        json.dump(result, file, indent=4)


def get_pilots(starship_info: dict) -> List[dict]:
    """
    Получает данные о пилотах корабля
    :param starship_info: Словарь, содержащий данные о корабле
    :return: Список всех пилотов корабля
    """
    result = []
    for pilot_url in starship_info['pilots']:
        pilot = requests.get(pilot_url)
        pilot_info = json.loads(pilot.text)
        result.append({
            'name': pilot_info['name'],
            'height': pilot_info['height'],
            'mass': pilot_info['mass'],
            'homeworld': get_homeworld_name(pilot_info['homeworld']),
            'homeworld_url': pilot_info['homeworld']
        })
    return result


def get_homeworld_name(homeworld_url: str) -> str:
    """
    Находит название родной планеты
    :param homeworld_url: URL адрес родной планеты
    :return: Название родной планеты
    """
    homeworld = requests.get(homeworld_url)
    return json.loads(homeworld.text)['name']


if __name__ == '__main__':
    get_starship_info('https://swapi.dev/api/starships/10/', 'millennium_falcon.json')
