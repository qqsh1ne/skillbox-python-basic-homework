class Stack:
    """
    Класс стека

    Attributes:
        __stack - значения стека
    """
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return '; '.join(self.__stack)

    def push(self, elem):
        """
        Добавляет элемент в конец стека
        :param elem: Элемент, который надо добавить
        :return: None
        """
        self.__stack.append(elem)

    def pop(self):
        """
        Удаляет и возвращает последний элемент стека

        :return: Последний элемент стека
        """
        return None if len(self.__stack) == 0 else self.__stack.pop()


class TaskManager:
    """
    Класс менеджера задач

    Attributes:
        tasks - словарь задач
    """
    def __init__(self):
        self.tasks = dict()

    def __str__(self):
        display = []
        if self.tasks:
            for i_priority in sorted(self.tasks.keys()):
                display.append(f'{str(i_priority)} {self.tasks[i_priority]}\n')

        return ''.join(display)

    def new_task(self, task, priority):
        """
        Добавляет новое задание в менеджер
        :param task: Добавляемая задача
        :param priority: Приоритет задачи
        """
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
