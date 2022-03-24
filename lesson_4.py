from datetime import datetime
import time

# Генератор списка

list = [i for i in range(1,35)]


# Функция генерации списка

def get_list(begin, end) -> list:
    return [i for i in range(begin,end)]




# Функция генерации списка текущего времени

def get_current_time():
    t = time.localtime()
    now_time = time.strftime("%H:%M:%S", t)
    return now_time

list = []
for i in range(1, 15):
    times = get_current_time()
    list.append(times)
print(list)
