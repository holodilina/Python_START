from logger import log


@log
def greetings():
    print('Добавить Список персонала')


@log
def show_menu():
    while True:
        try:
            value = int(input(
                '''\nВыберите команду:\n1 - Просмотреть весь список персонала.\n2 - Добавить сотрудника.\n3 - Изменить данные сотрудника.\n4 - Удалить сотрудника.\n0 - Выход.\n'''))
            if value > 4:
                print('Введите число от 0 до 4')
                continue
            elif value == 0:
                exit()
        except Exception:
            print('Неверный ввод')
        else:
            break
    return value


@log
def show_people(lst):
    print('Список всех сотрудников:\n')
    for index, item in enumerate(lst):
        if index == 0:
            print(' ', *item)
        else:
            print(index, *item)


@log
def show_create_data():
    data = input('Введите Фамилию, Имя, телефон и должность через пробел.\n').split()
    return data


@log
def show_upd_data():
    value = int(input('Введите ID сотрудника для изменения\n'))
    string = input('Введите новые данные: Фамилию, Имя, телефон и должность через пробел. \n').split()
    return value, string


@log
def show_del_data():
    value = int(input('Введите ID сотрудника для удаления.\n'))
    return value

