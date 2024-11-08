speed = 4096  # скорость передачи данных в байтах/cек
time = 120  # время в минутах затраченное на скачивание игры
cost = 0.125  # стоимость за один килобайт

speed_in_kb_in_sec =speed / 1024  # TODO перевести скорость скачивания из байт в килобайты, если 1 килобайт = 1024 байта
time_in_sec = time * 60  # TODO перевести время в секунды

free_traffic = 500  # количество бесплатного трафика
file_size = speed_in_kb_in_sec * time_in_sec # TODO размер файла
total_coast = cost * (file_size - free_traffic)  # TODO стоимость файла

print('Размер файла в килобайтах =', file_size)
print('За трафик придется заплатить:', total_coast)
