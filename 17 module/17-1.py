vowels = "аоиеёэыуюя"

text = input("Введите текст: ")
search_vowels = [char for char in text if char in vowels]

print("Список гласных букв:", search_vowels)
print("Длина списка:", len(search_vowels))