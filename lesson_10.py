class WrongSymbolException(Exception):

    def search_exception_mark(mark):
        marks = ('+', '-', '*', '**', '/', '//', '%')
        if mark != [symbol for symbol in marks]:
            print('Это что за символы? Я с ними работать не буду')

def get_data():
    first = float(input("Первое число: "))
    mark = input("Знак вычисления: ")
    second = float(input("Второе число: "))
    return first, mark, second

try:
    first, mark, second = get_data()
    if mark == '+':
        print(first+second)
    elif mark == '-':
        print(first-second)
    elif mark == '*':
        print(first*second)
    elif mark == '**':
        print(first**second)
    elif mark == '/':
        print(first/second)
    elif mark == '//':
        print(first//second)
    elif mark == '%':
        print(first%second)
    raise (WrongSymbolException)
    
except ZeroDivisionError:
    print('На ноль делить нельзя')

except TypeError as e:
    print(e)
    print('Кажется, был указан не тот знак при вводе')

except ValueError:
    print('Что за фигня? Тут должны быть цифры и знаки вычисления')

except WrongSymbolException:
    WrongSymbolException.search_exception_mark(mark=mark)