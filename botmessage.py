import csv
from telegram.ext import ConversationHandler
from model import open_phonebook, del_data, find_data


def start(update, context):
    update.message.reply_text(
        'Выберете команду:\
        \n/show - Показать справочник\
        \n/add - Добавить запись\
        \n/del - Удалить запись\
        \n/find - Найти запись\
        \nЕсли Вы случайно вошли в режим и не хотите вносить правки - введите /stop')
    return ConversationHandler.END


def bot_message_create_data(update, context):
    update.message.reply_text(
        f'Введите фамилию, имя, номер телефона и описание через пробел')
    return 1


def create_data(update, context):
    data = update.message.text.split()
    with open('file.csv', mode='a', encoding='utf-8', newline='') as file:
        write = csv.writer(file, delimiter=';')
        write.writerow(data)
    update.message.reply_text(
        f'Запись успешно добавлена')
    return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def show_phonebook(update, context):
    text = open_phonebook()
    update.message.reply_text(text)
    return ConversationHandler.END


def bot_message_del_data(update, context):
    text = open_phonebook()
    update.message.reply_text(
        f'Для удаления записи выберите ее номер.\n\n{text}')
    return 1


def bot_message_del_number(update, context):
    number = int(update.message.text)
    if del_data(number):
        update.message.reply_text(
            f'Запись №{number} успешно удалена')
    else:
        update.message.reply_text(f'Запись под номером {number} не существует')
    return ConversationHandler.END


def bot_message_find_data(update, context):
    update.message.reply_text(
        'Для поиска записи введите фамилию')
    return 1


def show_find_data(update, context):
    name = update.message.text
    find_name = find_data(name)
    if find_name:
        update.message.reply_text(f'Поиск по фамилии {name}:\n\n{find_name}')
    else:
        update.message.reply_text('Не найдено.')
    return ConversationHandler.END


def noname(update, context):
    update.message.reply_text('Такой команды нет.\
    \n/start для списка команд')
    return ConversationHandler.END