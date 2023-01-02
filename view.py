from logger import log


@log
def greatings():
    '''Приветствие.'''
    print('Справочник')


@log
def menu() -> int:
    """
    Вывод меню.
    """
    print('Меню')
    print(
        '0 - Выход \n1 - Загрузить из файла и вывести на экран \n2 - Добавить новую запись \n3 - Редактировать запись по id \n')
    return int(input("Введите пункт меню: "))


@log
def print_book(data: list):
    """
    Отображение справочника
    """
    for my_dict in data:
        print("id:", my_dict['id'])
        print("Имя:", my_dict['first_name'])
        print("Фамилия:", my_dict['last_name'])
        print("Телефон:", my_dict['phone_number'])
        print("Дата рождения:", my_dict['birthday'])
        print("Место работы:", my_dict['workplace'])
        print("----")
    if not data:
        print("<-Нет данных для отображения->")
        print()


@log
def add_record() -> dict:
    """
    Добавление нового контакта.
    """
    my_dict = {}

    my_dict['first_name'] = input('Напшите Имя : ')
    my_dict['last_name'] = input('Напишите Фамилия : ')
    my_dict['phone_number'] = input('Напишите Номер телефона: ')
    my_dict['birthday'] = input('Напишите Дата рождения: ')
    my_dict['workplace'] = input('Напишите Место работы: ')
    return my_dict


@log
def request_id() -> int:
    """
    Поиск
    """
    return int(input('Введите id: '))


@log
def editor(data: dict) -> dict:
    """
    Изменение контакта
    """
    # new_dict = {}
    data['first_name'] = input(f"Имя: {data['first_name']}. Введите новое имя: ")
    data['last_name'] = input(f"Фамилия: {data['last_name']} Введите новую фамилию: ")
    data['phone_number'] = input(f"Номер телефона: {data['phone_number']} Введите новый номер: ")
    data['birthday'] = input(f"Дата рождения: {data['birthday']} Введите новую дату: ")
    data['workplace'] = input(f"Место работы: {data['workplace']} Введите новое место работы: ")
    return data

