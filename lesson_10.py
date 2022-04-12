class WrongSymbol(Exception):

    def exception_mark(mark):
        marks = ('+', '-', '*', '**', '/', '//', '%')
        if mark != [symbol for symbol in marks]:
            print('Это что за символы? Я с ними работать не буду')

try:
    first = float(input("Первое число: "))
    mark = input("Знак вычисления: ")
    second = float(input("Второе число: "))
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
    else:
        WrongSymbol.exception_mark(mark=mark)
    
except ZeroDivisionError:
    print('На ноль делить нельзя')

except TypeError as e:
    print(e)
    print('Кажется, был указан не тот знак при вводе')

except ValueError:
    print('Что за фигня? Тут должны быть цифры и знаки вычисления')

# except WrongSymbol:
#     WrongSymbol.exception_mark(mark=mark)