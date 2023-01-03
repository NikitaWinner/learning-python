import os
import requests


PARSE_LOGS_FILE = os.path.join('data_file', 'pars_logs.txt')
NGINX_FILE = os.path.join('data_file', 'nginx_logs.txt')
USERS_FILE = os.path.join('data_file', 'users.csv')
HOBBIES_FILE = os.path.join('data_file', 'hobby.csv')
USERS_HOBBIES_FILE_JSON = os.path.join('data_file', 'task_6_3_result.json')
USERS_HOBBIES_FILE_TXT = os.path.join('data_file', 'task_6_4_result.txt')
BAKERY_FILE = os.path.join('data_file', 'bakery.csv')
NAMES_BAKERY_FILE = os.path.join('data_file', 'names_bakery_file.txt')


# Создание txt-файла со парсиными логами
def get_file_parse_logs(path_to_file: str) -> str:
    """Парсит файл и создает новый с txt-файл с результатами парсинга
    и возвращает созданый фаил в виде строки
    :param path: The path to the file to parse.
    :type path: str"""
    with open(path_to_file, 'w+', encoding='utf-8') as file_w:
        with open(NGINX_FILE, 'r+', encoding='utf-8') as file_r:
            content = (f'{line.split()[0], line.split()[5][1:], line.split()[6]}' for line in file_r)
            for el in content:
                print(el, file=file_w)
        file_w.seek(0)
        str_file = file_w.read()
    return str_file

# Создание txt-файла с логами
def get_file_nginx(path_to_file: str):
    """Функция создает txt файл логами nginx
    параметр name_file: принимает путь, по которому создастся  txt-файл
    и возвращает созданый фаил ввиде строки"""

    with open(path_to_file, 'w+', encoding='utf-8') as file:
        response = requests.get(
            'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
        file.write(response.text)
        file.seek(0)
        str_file = file.read()
    return str_file


# Создание csv-файла c ФИО
def get_file_random_users(path_to_file: str):
    """Функция создает csv файл с рандомными ФИО в количество 100
    и возвращает этот фаил в виде строки
    параметр name_file: принимает путь, по которому создастся  csv файла"""

    responce = requests.get('https://randomus.ru/name?type=0&sex=10&count=100')
    list_users = responce.text[responce.text.find('data-numbers=')+len('data-numbers=') + 1:
                             responce.text.find('</textarea>')].splitlines()[1:]
    with open(path_to_file, 'w+', encoding='utf-8') as file:
        for el in list_users:
            file.write(f"{el.replace(' ', ',')}\n")
        file.seek(0)
        str_file = file.read()
    return str_file


# Создание csv-файла c хобби
def get_file_hobbies(path_to_file: str):
    """Функция создает csv файл сo > 100 строковых значений хобби
    и возвращает созданный фаил в виде строки
    параметр name_file: принимает путь, по которому создастся  csv файла"""

    responce = requests.get('http://vatolin.info/texts/56-psychologist-client/391-giant-list-of-hobbies-and-pleasures?fbclid=IwAR2y1Q6-QR21yU8JG0qEet_DX6vYtpyFFeny4JCPgO3ejlw-R1fi3MmeZMM')
    list_hobby = responce.text[responce.text.find('<li>Автомобили</li>'):
                               responce.text.find('<li>Шитье и вышивание</li>')]\
                                .replace('<li>', '').replace('</li>', '')\
                                .replace('\r', '').replace('&hellip;', '').split('\n')
    with open(path_to_file, 'w+', encoding='utf-8') as file:
        for el in list_hobby:
            file.write(f"{el.replace('(', ',').replace(')', '').replace(', ', ',').replace(' ,', ',')}\n")
        file.seek(0)
        str_file = file.read()
    return str_file


def create_user_file(users: str, hobbies: str, path: str):
    """Функция создает txt-файл с логами и хобби
     в формате ф,и,о: хобби,хобби"""
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'{users.strip()}: {hobbies}')


# def create_file_csv(filename):
#     """Функция проверяет наличие и создаёт csv-фаил
#     :param filename:
#     :return:
#     """
#     if not add_sale.check_file(filename):
#         path_to_file = os.path.join("data", filename)
#         with open(path_to_file, 'w', encoding='utf-8') as file:
#             with open(NAMES_BAKERY_FILE, 'a', encoding='utf-8') as file_2:
#                 file_2.write(f'{filename}\n')
#         print(f'Done! File named {filename} created.')
#     else:
#         print(f'File named {filename} already exists.')
#



if __name__ == '__main__':
    # get_file_random_users(USERS_FILE)
    # get_file_hobbies(HOBBIES_FILE)
    # get_file_nginx(NGINX_FILE)
    # get_file_parse_logs(PARSE_LOGS_FILE)

    print('Done')