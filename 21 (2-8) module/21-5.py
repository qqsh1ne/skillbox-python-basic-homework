def calculating_math_func(data: int, factorial={0: 1}):
    if data in factorial:
        result = factorial.get(data)
    else:
        for index in range(max(factorial) + 1, data + 1):
            result = factorial.get(max(factorial))
            result *= index
            factorial.update({index: result})
        return calculating_math_func(data, factorial)

    result /= data ** 3
    result = result ** 10
    return result


result = calculating_math_func(int(input('Введите число: ')))
print(result)
