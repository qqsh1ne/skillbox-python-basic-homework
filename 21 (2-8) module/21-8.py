def flatten(a_list):
    result = []
    for element in a_list:
        if isinstance(element, int):
            result.append(element)
        else:
            result.extend(flatten(element))
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ:', flatten(nice_list))
