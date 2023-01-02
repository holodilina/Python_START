from logger import log
import json


@log
def get_data() -> list:
    """
    Считывание словаря из файла
    """
    with open("Contacts.json", "r", encoding="utf-8") as file:
        data_file = json.load(file)
    return data_file["items"]


@log
def get_data_id(id: int) -> dict:
    """
    1 запись по id
    """
    with open("Contacts.json", "r", encoding="utf-8") as file:
        data_file = json.load(file)
        for item in data_file['items']:
            if item['id'] == id:
                return item


@log
def add_data(data: dict):
    """
    Добавление контакта.
    """
    id = data.get("id")

    with open("Contacts.json", "r", encoding="utf-8") as file:
        data_file = json.load(file)

    if id:
        for i, items in enumerate(data_file["items"]):
            if id == items["id"]:
                data_file["items"][i] = data
                break

    else:
        id = data_file["last_id"]["id"] + 1
        data_file["last_id"]["id"] = id
        data["id"] = id
        data_file["items"].append(data)

    with open("Contacts.json", "w", encoding="utf-8") as file:
        json.dump(data_file, file, indent=2, ensure_ascii=False)

