import csv
import os
from logger import log


@log
def get_people():
    if os.path.isfile('personal.csv'):
        with open('personal.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            return list(reader)
    else:
        print("Список сотрудников еще не создан.")
        exit()


@log
def create_data(lst):
    file_path = 'personal.csv'
    if not os.path.exists(file_path):
        with open('personal.csv', mode='a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Фамилия', 'Имя', 'Телефон', 'Должность'])
    with open('personal.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(lst)


@log
def update_data(num, string):
    try:
        with open('personal.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            data = list(reader)
            data[num] = string
        with open('personal.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print('Сотрудника с таким ID в списке нет')


@log
def del_data(num):
    try:
        with open('personal.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            data = list(reader)
            del data[num]
        with open('personal.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print('Сотрудника с таким ID в списке нет')

