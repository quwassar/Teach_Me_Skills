marks = ('+', '-', '*', '**', '/', '//', '%')

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
    
except ZeroDivisionError:
    print('На ноль делить нельзя')

except TypeError:
    print('Кажется, был указан лишний знак при вводе')

except ValueError:
    print('Что за фигня? Тут должны быть цифры и знаки вычисления')

except Exception:
    print('Test')