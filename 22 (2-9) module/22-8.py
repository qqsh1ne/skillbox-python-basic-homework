def get_frequency(text):
    chars_dict = {}
    chars_count = 0

    for char in text:
        if ord('a') <= ord(char) <= ord('z'):
            chars_dict[char] = chars_dict.get(char, 0) + 1
            chars_count += 1

    frequency = [(char, "{:5.3f}".format(chars_dict[char] / chars_count)) for char in chars_dict.keys()]
    frequency.sort(key=lambda x: x[0])
    frequency.sort(key=lambda x: x[1], reverse=True)
    return frequency


text = open("text.txt", "r").read().lower()

analysis = open("analysis.txt", "w")
analysis.write("\n".join([char_data[0] + " " + char_data[1] for char_data in get_frequency(text)]))
analysis.close()
