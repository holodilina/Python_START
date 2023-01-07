import csv
import os


def open_phonebook():
    if not os.path.exists('file.csv'):
        with open('file.csv', mode='w', encoding='utf-8', newline='') as file:
            write = csv.writer(file, delimiter=';')
            write.writerow(['Фамилия', 'Имя', 'Телефон', 'Заметка'])
        return 'Ваш справочник пуст, добавьте данные командой /add'
    with open('./file.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        text = ''
        for index, item in enumerate(reader):
            if index == 0:
                index = ' '
            text += f'{index} - ' + ' '.join(item) + '\n'
    return text


def del_data(number):
    with open('./file.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        data = list(reader)
        if number != 0 and number < len(data):
            del data[number]
            with open('./file.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                for i in data:
                    writer.writerow(i)
            return True
        else:
            return False


def find_data(name):
    with open('./file.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        data = list(reader)
    text = ''
    for item in data:
        if name in item[0]:
            text += ' '.join(item) + '\n'
    return text