class Node:
    """
    Элемент односвязного списка

    Args:
        value - значение элемента

    Attributes:
        value - значение элемента
        next_node - следующий элемент
    """
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    """
    Односвязный список

    Attributes:
        __head - 'Головной' элемент
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        if self.__head is None:
            return '[]'
        current_node = self.__head
        string = ''
        while current_node:
            string += str(current_node.value) + ' '
            current_node = current_node.next_node
        return '[' + string[:-1] + ']'

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.value
            current = current.next_node

    def append(self, value):
        """
        Добавляет элемент в конец односвязного списка

        :param value: Значение нового элемента
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        else:
            current = self.__head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(value)

    def get(self, index):
        """
        Получает элемент списка по индексу
        
        :param index: Индекс элемента
        :return: Значение полученного элемента списка
        """
        if self.__head is None:
            raise IndexError('Индекс вне границ списка')
        else:
            count = 0
            current = self.__head
            while current:
                if index == count:
                    return current.value
                current = current.next_node
                count += 1
            else:
                raise IndexError('Индекс вне границ списка')

    def remove(self, index):
        """
        Удаляет элемент по индексу
        
        :param index: Индекс удаляемого элемента
        """
        if self.__head is not None:
            if index == 0:
                self.__head = self.__head.next_node
                return
            count = 1
            current = self.__head.next_node
            prev = self.__head
            while current:
                if index == count:
                    if current.next_node is None:
                        prev.next_node = None
                        return
                    prev.next_node = current.next_node
                    return
                prev = current
                current = current.next_node
                count += 1
            else:
                raise IndexError('Индекс вне границ списка')
        else:
            raise IndexError('Индекс вне границ списка')


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('Текущий список:', my_list)
for elem in my_list:
    print(elem)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
