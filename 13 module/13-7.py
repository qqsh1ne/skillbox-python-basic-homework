def get_danger(depth):
    return depth ** 3 - 3 * depth ** 2 - 12 * depth + 10


def get_safe_depth(danger_max):
    depth_max = 4
    depth_min = 0
    depth = depth_min + (depth_max - depth_min) / 2

    danger = get_danger(depth)

    while abs(danger) > danger_max:
        if danger > 0:
            depth_min = depth
        else:
            depth_max = depth
        depth = depth_min + (depth_max - depth_min) / 2
        danger = get_danger(depth)
    return depth


danger_max = float(input('Введите максимально допустимый уровень опасности: '))
while danger_max < 0:
    print('Макс. опасность должна быть абсолютной и не менее нуля')
    danger_max = float(input('Введите максимально допустимый уровень опасности: '))

print('Приблизительная глубина безопасной кладки:', get_safe_depth(danger_max))
