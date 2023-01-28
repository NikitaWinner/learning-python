import os
import sys
import json
from itertools import zip_longest
from create_file import create_user_file, USERS_FILE, HOBBIES_FILE, USERS_HOBBIES_FILE_TXT


def prepare_dataset(path_users_file: str, path_hobby_file: str, path_out_file: str):
    """
    Считывает данные из csv-файлов где
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: None
    """
    with open(path_users_file, 'r', encoding='utf-8') as file_users:
        with open(path_hobby_file, 'r', encoding='utf-8') as file_hobbies:
            while True:
                line_user = file_users.readline()
                line_hobby = file_hobbies.readline()
                if not line_hobby:
                    line_hobby = None
                    if not line_user:
                        break
                else:
                    if not line_user:
                        sys.exit(1)
                create_user_file(line_user, line_hobby, path_out_file)

if __name__ == '__main__':
    prepare_dataset(USERS_FILE, HOBBIES_FILE, USERS_HOBBIES_FILE_TXT)