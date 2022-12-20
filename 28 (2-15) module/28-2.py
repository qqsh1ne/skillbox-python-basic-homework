import math


class MyMath:
    """
    Класс для работы с геометрическими объектами
    """
    @classmethod
    def circle_len(cls, r: float) -> float:
        """
        Высчитывает длину окружности

        :param r: Радиус окружности

        :return: Длина окружности
        """
        return 2 * r * math.pi

    @classmethod
    def circle_sq(cls, r: float) -> float:
        """
        Высчитывает площадь окружности

        :param r: Радиус окружности

        :return: Площадь окружности
        """
        return r ** 2 * math.pi

    @classmethod
    def cube_vol(cls, edge: float) -> float:
        """
        Высчитывает объём куба
        :param edge: Сторона куба
        :return: Объём куда
        """
        return (2 * edge) ** 3

    @classmethod
    def sphere_sq(cls, r: float) -> float:
        """
        Высчитывает площадь сферы

        :param r: Радиус сферы

        :return: Площадь сферы
        """
        return r ** 2 * math.pi * 4

    @classmethod
    def sphere_vol(cls, r: float) -> float:
        """
        Высчитывает объём сферы

        :param r: Сторона сферы
        :return: Объём сферы
        """
        return 4 / 3 * math.pi * r ** 3


print(MyMath.circle_len(5))
print(MyMath.circle_sq(6))
print(MyMath.cube_vol(7))
print(MyMath.sphere_sq(8))
print(MyMath.sphere_vol(9))
