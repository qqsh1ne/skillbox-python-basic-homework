import json


diff_list = ['services', 'staff', 'datetime']


def compare_two_jsons(json_1, json_2):
    """
    Позволяет сравнить два json файла по указанным в diff_list ключам
    :param json_1: Первый json файл
    :param json_2: Второй json файл
    :return: Их различия
    """
    result = {}
    for key, value in json_1.items():
        if type(value) == dict:
            result.update(compare_two_jsons(json_1[key], json_2[key]))
        if key not in diff_list:
            continue
        if value != json_2[key]:
            result[key] = json_2[key]
    return result


with open('json_old.json', 'r', encoding="UTF-8") as file:
    json_old = json.load(file)

with open('json_new.json', 'r', encoding="UTF-8") as file:
    json_new = json.load(file)

res = compare_two_jsons(json_old, json_new)
print(res)
with open('json_diffs.json', 'w', encoding="UTF-8") as file:
    json.dump(res, file, indent=4, ensure_ascii=False)
