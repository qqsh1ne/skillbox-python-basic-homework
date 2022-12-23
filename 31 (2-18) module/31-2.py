import re

if __name__ == '__main__':
    pattern_personal = r"\b[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]\d{3}[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]{2}\d{2,3}"
    pattern_taxi = r"\b[А, В, Е, К, М, Н, О, Р, С, Т, У, Х]{2}\d{5,6}"
    numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    print("Список номеров частных автомобилей:", re.findall(pattern_personal, numbers))
    print("Список номеров такси:", re.findall(pattern_taxi, numbers))
