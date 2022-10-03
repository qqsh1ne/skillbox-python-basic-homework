num = int(input("Введите любое четырёхзначное число: "))
a = num % 10
b = num // 10 % 10
c = num // 100 % 10
d = num // 1000 % 10
print(d, c, b, a)