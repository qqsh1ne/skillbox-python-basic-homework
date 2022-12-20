import random


class Person:
    """
    Класс человека

    Args:
        name - имя человека
        surname - фамилия человека
        age - возраст человека

    Attributes:
        __name - имя человека
        __surname - фамилия человека
        __age - возраст человека
    """
    def __init__(self, name: str, surname: str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Сотрудник {self.__name} {self.__surname}.'

    @staticmethod
    def generate_person():
        """
        Создает человека с рандомными аргументами

        :return: Человек со случайными данными

        :rtype: Person
        """
        name = random.choice(names)
        surname = random.choice(surnames)
        age = random.randint(20, 80)
        return name, surname, age


class Employee(Person):
    """
    Класс сотрудника. Родитель - Person

    Args:
        name - имя человека
        surname - фамилия человека
        age - возраст человека

    Attributes:
        __name - имя человека
        __surname - фамилия человека
        __age - возраст человека
    """
    def calc_salary(self):
        """
        Высчитывает зарплату сотрудника

        :return: Зарплата сотрудника
        """
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f' Должность: {self.__class__.__name__}. Зарплата: {self.calc_salary()}'


class Manager(Employee):
    """
    Класс менеджера. Родитель - Employee

    Args:
        name - имя человека
        surname - фамилия человека
        age - возраст человека

    Attributes:
        __name - имя человека
        __surname - фамилия человека
        __age - возраст человека
    """
    def calc_salary(self):
        """
        Высчитывает зарплату менеджера

        :return: Зарплата менеджера
        :rtype: int
        """
        return 13000


class Agent(Employee):
    """
    Класс агента. Родитель - Employee

    Args:
        name - имя человека
        surname - фамилия человека
        age - возраст человека
        sales - объем продаж

    Attributes:
        __name - имя человека
        __surname - фамилия человека
        __age - возраст человека
        __sales - объем продаж
    """
    def __init__(self, name: str, surname: str, age: int, sales: int):
        super().__init__(name, surname, age)
        self.__sales = sales

    def calc_salary(self):
        """
        Высчитывает зарплату агента
        :return: Зарплата агента
        :rtype: int
        """
        return 5000 + 0.05 * self.__sales


class Worker(Employee):
    """
    Класс работника. Родитель - Employee

    Args:
        name - имя человека
        surname - фамилия человека
        age - возраст человека
        hours - кол-во отработанных часов

    Attributes:
        __name - имя человека
        __surname - фамилия человека
        __age - возраст человека
        __hours - кол-во отработанных часов
    """
    def __init__(self, name: str, surname: str, age: int, hours: int):
        super().__init__(name, surname, age)
        self.__hours = hours

    def calc_salary(self):
        """
        Высчитывает зарплату агента
        :return: Зарплата агента
        :rtype: int
        """
        return 100 * self.__hours


names = ['Кен', 'Гоша', 'Ваня', 'Эль', 'Шелли', 'Найс', 'Падж']
surnames = ['Канеки', 'Рубчинский', 'Примо', 'Крутой', 'Играешь', 'Лефрутов']

employees = list()

for _ in range(3):
    employees.append(Manager(*Person.generate_person()))

for _ in range(3):
    agent = Agent(*Person.generate_person(), random.randint(2000, 10000))
    employees.append(agent)

for _ in range(3):
    worker = Worker(*Person.generate_person(), random.randint(20, 50))
    employees.append(worker)

for employee in employees:
    print(employee)
