def tpl_sort(origin_tuple):
    for element in origin_tuple:
        if element != int(element):
            return origin_tuple
    return tuple(sorted(list(origin_tuple)))


# print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
