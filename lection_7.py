import re
import json
import csv

pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'


def checker(func):
    def wrapper():
        print("1. Registration")
        print("2. Autorization")
        answer = input("Input your choise: ")
        answer = int(answer)
        i = True
        while i:
            data = func()
            if answer == 1:
                if re.match(pattern, data[0]) is not None:
                    if data[1] == data[0]:
                        print("Пароль не должен совпадать с email")
                    else:
                        if re.match(pattern_password, data[1]) is not None:
                            print("Password correct")
# Text file
                            # with open('users.txt', 'a') as users_file:
                            #     users_file.write(f'{data[0]}\n{data[1]}\n')
# JSON file
                            # data_json = {'email': data[0], 'passwd': data[1]}
                            # with open('users.json', 'a') as users_file:
                            #     json.dump(data_json, users_file)
# CSV file
                            with open('users.csv', 'a', newline='') as users_file:
                                fieldnames = ['email', 'passwd']
                                users_writer = csv.DictWriter(users_file, fieldnames=fieldnames)
                                users_writer.writerow(data)
                            i = False
                        else:
                            print("Пароль некорректен, он должен быть больше 8 знаков и содержать большие буквы, цифры и спец знаки")
                else:
                    print('Необходимо указать корректный email')
            if answer == 2:
# Text file
                # with open('users.txt', 'r') as users_file:
                #     lines = users_file.readlines()
                #     for line in lines:
                #         if lines[0] == f'{data[0]}\n':
                #             if lines[1] == f'{data[1]}\n':
                #                 print('Data success!')
                #             else:
                #                 print("Password incorrect")
                #         else:
                #             print('Email incorrect')
# JSON file
                # with open('users.json', 'r') as users_file:
                #     data_file = json.loads(users_file.read())
                #     for line in data_file:
                #         if data[0] == line['email']:
                #             if data[1] == line['passwd']:
                #                 print('Data success!')
                #                 i = False
                #             else:
                #                 print("Password incorrect")
                #         else:
                #             print('Email incorrect')

                with open('users.csv', 'r') as users_file:
                    data_file = csv.reader(users_file, delimiter=',')
                    for line in data_file:
                        if data[0] == line[0]:
                            if data[1] == line[1]:
                                print('Data success!')
                                i = False
                            else:
                                print("Password incorrect")
                        else:
                            print('Email incorrect')
    return wrapper


@checker
def input_email():
    email = input("Input your email: ")
    password = input('Input your password: ')
    return email, password


input_email()



