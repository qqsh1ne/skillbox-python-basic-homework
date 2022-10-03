file_size = float(input('Укажите размер файла для скачивания: '))
network_speed = float(input('Какова скорость вашего соединения? '))
time_download = round(file_size / network_speed)
download, percent = 0, 0

for time in range(1, time_download + 1):
    download += network_speed
    percent = round(download / file_size * 100)
    if time == time_download:
        download = file_size
        percent = 100
    print(f'Прошло {time} сек. Скачано {round(download)} из {round(file_size)} Мб ({str(percent)}%)')