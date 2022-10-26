first = [1, 2, 3, 4, 123123123123]
second = (10, 20, 12, 40)

pairs = ((first[i_element], second[i_element]) for i_element in range(min(len(first), len(second))))

print(pairs)
for i_element in pairs:
    print(i_element)