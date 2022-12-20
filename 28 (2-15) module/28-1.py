class File:
    """
    Класс файла.

    Args:
        file_name - название файла

    Attributes:
        file_name - название файла
    """
    def __init__(self, file_name: str):
        self.file_name = file_name

    def __enter__(self):
        try:
            self.file = open(self.file_name, 'r')
        except FileNotFoundError:
            self.file = open(self.file_name, 'w')
        finally:
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

    def write(self, value: str) -> None:
        """
        Записывает значение в файл

        :param value: Значение, которое нужно записать
        """
        self.file.write(value)


with File('test.txt') as my_file:
    my_file.write('Test')
