def crypto(checking_list):
    return [element for index, element in enumerate(checking_list) if is_prime(index)]


def is_prime(i_num):
    k = 0
    for i in range(1, i_num // 2 + 1):
        if i_num % i == 0:
            k = k + 1
    return True if k == 1 else False


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))