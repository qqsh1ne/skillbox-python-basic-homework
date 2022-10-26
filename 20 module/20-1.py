def print_pairs():
    pairs = []
    for i_id, i_student in students.items():
        pairs.append((i_id, i_student['age']))
    print(pairs)


def get_interests(students):
    surnames_length = 0
    interests = set()
    for i_value in students.values():
        surnames_length += len(i_value['surname'])
        for interest in i_value['interests']:
            interests.add(interest)

    return interests, surnames_length


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

print_pairs()
interests, surnames_length = get_interests(students)
print(f'{interests}\n{surnames_length}')
