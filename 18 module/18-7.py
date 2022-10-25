ip_elements = input('Введите IP: ').split('.')

if len(ip_elements) != 4:
    print('Адрес - это четыре числа, разделённые точками')
    exit()

for x in ip_elements:
    if not x.isdigit():
        print(x, '- не целое число')
        exit()
    if int(x) > 255:
        print(x, 'превышает 255')
        exit()
        
print('IP-адрес корректен')