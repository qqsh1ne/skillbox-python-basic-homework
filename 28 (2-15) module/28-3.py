class Date:
    """
    Класс для работы с датой

    Args:
        day - день
        month - месяц
        year - год

    Attributes:
        day - день
        month - месяц
        year - год
    """
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day}\tМесяц: {self.month}:\tГод: {self.year}'

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        """
        Валидирует дату
        :param date: Дата
        :return: Валидна ли дата
        """
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        """
        Конвертирует строку даты в объект класса Date
        :param date: Строка с датой
        :return: Объект типа Data
        """
        day, month, year = map(int, date.split('-'))
        return cls(day, month, year)


my_date = Date.from_string('10-12-2077')
print(my_date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
