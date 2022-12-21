from collections import Counter


def can_be_poly(string: str) -> bool:
    """
    Проверяет, может ли строка быть палиндромом

    :param string: Строка, которую необходимо проверить

    :return: Может строка быть палиндромом или нет
    """
    return len(list(filter(lambda x: x % 2, Counter(string).values()))) <= 2


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))
