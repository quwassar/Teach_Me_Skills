from datetime import datetime
import time

# Генератор списка

list = [i for i in range(1,35)]


# Функция генерации списка

def get_list(end) -> list:
    return [i for i in range(end)]



# Функция генерации списка текущего времени

def get_current_time():
    t = time.localtime()
    now_time = time.strftime("%H:%M:%S", t)
    return now_time

end = 40
list = [get_current_time() for i in range(1, end)]


