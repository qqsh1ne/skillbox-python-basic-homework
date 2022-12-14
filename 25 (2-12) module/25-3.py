class MyDict(dict):
    """
    Класс словаря и измененным методом get. Родитель: dict.
    """
    def get(self, key):
        """
        Возвращает элемент по ключу, если не находит такой ключ, то возвращает 0

        :return: значение ключа key
        """
        return super().get(key, 0)


my_dict = MyDict({'один': 1, 'два': 2})
print(my_dict.get('один'))
print(my_dict.get('два'))
print(my_dict.get('три'))
print(my_dict.get('четыре'))
