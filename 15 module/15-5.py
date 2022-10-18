films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favourite_films = []
adding_films_amount = int(input('Сколько фильмов хотите добавить? '))

for _ in range(adding_films_amount):
    film_name = input('Введите название фильма: ')
    if film_name in films:
        favourite_films.append(film_name)
    else:
        print(f'Ошибка: фильма {film_name} у нас нет :(')

print('Ваш список любимых фильмов:', favourite_films)