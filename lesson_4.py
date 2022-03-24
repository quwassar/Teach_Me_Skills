from datetime import datetime
import time

# Генератор списка

list = [i for i in range(1,35)]


# Функция генерации списка

def get_list() -> list:
    list = [i for i in range(8,79)]
    return list

list = get_list()


# Функция генерации списка текущего времени

def get_current_time():
    list = []
    for i in range(1, 10):
        t = time.localtime()
        now_time = time.strftime("%H:%M:%S", t)
        list.append(now_time)
    return list
