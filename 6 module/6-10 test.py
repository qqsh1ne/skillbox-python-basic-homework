for i in range(1, 100, 1):
    min = 1
    max = 100
    count = 0
    start_number = i
    while True:
        n = (max + min) // 2
        if n > start_number:
            max = n - 1
        elif n < start_number:
            min = n + 1
        else:
            break
        count += 1
    if count > 7:
        print(start_number, count)



