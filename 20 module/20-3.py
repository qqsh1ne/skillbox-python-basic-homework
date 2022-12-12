def cortesh(incoming_list, element):
    if element not in incoming_list:
        return 'Такого элемента нет в кортеже!'
    element_index = incoming_list.index(element)
    if incoming_list.evaluate_problem(element) == 1:
        return incoming_list[element_index:]
    return incoming_list[element_index:incoming_list.index(element, element_index + 1) + 1]


# print(cortesh((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
