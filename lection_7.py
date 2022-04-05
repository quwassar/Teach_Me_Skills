import csv
import re
import json

pattern_email = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'


def write_txt(data):
    with open('users.txt', 'a') as users_file:
        users_file.write(f'{data[0]}\n{data[1]}\n')
    print('Write success')
    return False


def write_json(data):
    data_json = {'email': data[0], 'passwd': data[1]}
    with open('users.json', 'a') as users_file:
        json.dump(data_json, users_file)
    print('Write success')
    return False


def write_csv(data):
    with open('users.csv', 'a', newline='') as users_file:
        fieldnames = ['email', 'passwd']
        users_writer = csv.DictWriter(users_file, fieldnames=fieldnames)
        users_writer.writerow({'email':data[0], 'passwd': data[1]})
        print('Write success')
    return False


def open_txt(data):
    with open('users.txt', 'r') as users_file:
        lines = users_file.readlines()
        for line in lines:
            if line[0] == f'{data[0]}\n':
                if line[1] == f'{data[1]}\n':
                    print('Data success!')
                    while_status = False
                else:
                    print("Password incorrect")
                    while_status = True
            else:
                print('Email incorrect')
                while_status = True
    return while_status


def open_json(data):
    with open('users.json', 'r') as users_file:
        data_file = json.load(users_file)
        if data[0] == data_file['email']:
            if data[1] == data_file['passwd']:
                print('Data success!')
                while_status = False
            else:
                print("Password incorrect")
                while_status = True
        else:
            print('Email incorrect')
            while_status = True
    return while_status


def open_csv(data):
    with open('users.csv', 'r') as users_file:
        data_file = csv.reader(users_file, delimiter=',')
        for line in data_file:
            if data[0] == line[0]:
                if data[1] == line[1]:
                    print('Data success!')
                    while_status = False
                else:
                    print("Password incorrect")
                    while_status = True
            else:
                print('Email incorrect')
                while_status = True
    return while_status


def choiser(data, answer):
    if answer == 1:
        if re.match(pattern_email, data[0]) is not None:
            if data[1] == data[0]:
                print("Пароль не должен совпадать с email")
            else:
                if re.match(pattern_password, data[1]) is not None:
                    print("Password correct \nHow i need write data? \n1. Text \n2. JSON \n3. CSV")
                    answer_write = int(input('Input you choise: '))
                    if answer_write == 1:
                        while_status = write_txt(data)
                    elif answer_write == 2:
                        while_status = write_json(data)
                    elif answer_write == 3:
                        while_status = write_csv(data)
                    else:
                        print('Choise incorrect')
                        while_status = True
                else:
                    print("Пароль некорректен, он должен быть больше 8 знаков и содержать большие буквы, цифры и спец знаки")
                    while_status = True
        else:
            print('Необходимо указать корректный email')
            while_status = True
    if answer == 2:
        answer_open = int(input('What file i need open? \n1. TXT \n2. JSON \n3. CSV \nInput your choise: '))
        print(answer_open, type(answer_open))
        if answer_open == 1:
            while_status = open_txt(data)
        elif answer_open == 2:
            print(data, type(data))
            while_status = open_json(data)
        elif answer_open == 3:
            while_status = open_csv(data)
        else:
            print('Input correct choise')
            while_status = True
    return while_status


def checker(func):
    def wrapper(*args, **kwargs):
        print("""1. Registration \n2. Autorization""")
        answer = int(input("Input your choise: "))
        data = func()
        while_status = True
        while while_status:
            try:
                while_status = choiser(data, answer)
            except Exception as e:
                print(e)
    return wrapper

@checker
def input_email():
    email = input("Input your email: ")
    password = input('Input your password: ')
    return [email, password]


input_email()



