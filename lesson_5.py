# Создать свой декоратор 

def get_hello(func):
    """ Просто добавляет текст после вызова основной функции """
    name = func()
    print(f'Hello, {name}. This is decorator')

@ get_hello
def get_name():
    """ Просит ввести имя пользователя """
    name = input("Input your name: ")
    return name


# Сделать lambda функцию

list_name = ["Michail", "Anatoliy", "Sergey"]


def get_hello_for_list(list_name):
    """Функция получает список имён и добавляет Hello к ним"""
    print(list(map(lambda name: "Hello " + name, list_name)))

get_hello_for_list(list_name)

