site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def make_new_site(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = make_new_site(sub_struct, key, meaning)
            if result:
                return site


number_sites = int(input('Сколько сайтов: '))
for _ in range(number_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    keys = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
    for key in keys:
        print(key)
        make_new_site(site, key, keys[key])

    print(f'Сайт для {product_name}:')
    print(site, '\n')
