summ = 0
tmp_str = ''
numbers = open('numbers.txt', 'r')
for row in numbers:
    tmp_str = list(map(int, row.split()))
    if tmp_str != '':
        summ += int(sum(tmp_str))
numbers.close()
answer = open('answer.txt', 'w')
answer.write(str(summ))
answer.close()
