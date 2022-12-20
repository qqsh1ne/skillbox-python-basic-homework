class Property:
    """
    Базовый класс имущества.

    Args:
        worth: стоимость имущества

    Attributes:
        __worth: стоимость имущества
    """
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        """
        Геттер для получения стоимости имущества.
        :return: __worth
        :rtype: float
        """
        return self.__worth

    def get_tax(self):
        """
        Высчитывает налог на данное имущество

        :return: Налог на имущество
        :rtype: float
        """
        raise Exception('This method must be overriden')


class Apartment(Property):
    """
    Класс квартиры. Родитель: Property

    Args:
        worth: стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Высчитывает налог на данное имущество

        :return: Налог на имущество
        :rtype: float
        """
        return self.get_worth() / 1000


class Car(Property):
    """
    Класс машины. Родитель: Property

    Args:
        worth: стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Высчитывает налог на данное имущество

        :return: Налог на имущество
        :rtype: float
        """
        return self.get_worth() / 200


class CountryHouse(Property):
    """
    Класс дома. Родитель: Property

    Args:
        worth: стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Высчитывает налог на данное имущество

        :return: Налог на имущество
        :rtype: float
        """
        return self.get_worth() / 500


while True:
    my_property_number = int(input('Выберите имущество:\n' +
                        '1 - Дом\n' +
                        '2 - Автомобиль\n' +
                        '3 - Дача\n' +
                        '0 - Выход\n'))
    if my_property_number not in (0, 1, 2, 3):
        print('Введите верное значение.')
        continue
    if my_property_number == 0:
        exit()
    cash = float(input('Имеется денег: '))
    worth = float(input('Стоимость имущества: '))

    my_property = Apartment(worth) if my_property_number == 1 \
        else Car(worth) if my_property_number == 2  \
        else CountryHouse(worth)
    tax = my_property.get_tax()
    print(f'Налог на имущество: {tax}')
    money_left = 0 if cash >= tax else my_property.get_tax() - cash

    print(f'Необходимо ещё денег: {money_left}\n')
