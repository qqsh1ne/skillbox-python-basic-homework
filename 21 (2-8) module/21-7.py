def summ(*args):
    def flatten(a_list):
        result = []
        for element in a_list:
            if isinstance(element, int):
                result.append(element)
            else:
                result.extend(flatten(element))
        return result
    return sum(flatten(args))