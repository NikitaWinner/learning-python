import os
import sys
import json
from itertools import zip_longest
from create_file import USERS_FILE, HOBBIES_FILE, USERS_HOBBIES_FILE_JSON


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    with open(path_users_file, 'r', encoding='utf-8') as file:
        list_users = [el.replace(',', ' ') for el in file.read().splitlines()]

    with open(path_hobby_file, 'r', encoding='utf-8') as file:
        list_hobby = [el.split(',') for el in file.read().split('\n')]

    if len(list_users) <= len(list_hobby):
        return {key: value for key, value in zip_longest(list_users, list_hobby)}
    else:
        sys.exit(1)


# Создание json файла c ФИО и хобби
dict_out = prepare_dataset(USERS_FILE, HOBBIES_FILE)
with open(USERS_HOBBIES_FILE_JSON, 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=4)
