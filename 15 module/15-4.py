def find_left_gpus():
    left_gpus = []
    for gpu in gpus:
        if gpu < max_gpu_number:
            left_gpus.append(gpu)
    return left_gpus


gpu_amount = int(input('Количество видеокарт: '))
gpus = []
max_gpu_number = -1

for i_gpu in range(gpu_amount):
    print(i_gpu + 1, 'Видеокарта: ', end='')
    gpu_number = int(input())
    gpus.append(gpu_number)
    if gpu_number > max_gpu_number:
        max_gpu_number = gpu_number


print('Старый список видеокарт:', gpus)
print('Новый список видеокарт:', find_left_gpus())