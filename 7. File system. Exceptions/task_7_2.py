import os
import yaml


def create_project_starter(config_file_name: str):
    """
    Функция для создания структуры папок и файлов в соответствии с файлом конфигурации.
    Файл должен иметь следующую структуру:
    - каждая строка - отдельная папка или файл
    - файл отличается от папки наличием точки
    - количетво символов "пробел" перед названием папки или файла определяет его уровень вложенности
    - БУДЬТЕ ВНИМАТЕЛЬНЫ: не допускается ситуация, когда уровень вложенности текущего элемента больше
    уровня вложенности предыдущего элемента более, чем на 1
    :param config_file_name: имя yaml-файла с конфигурацией
    :return: None
    """

    with open(config_file_name) as f:
        path_items_list = []  # список для хранения элементов пути
        prev_level = -1  # стартовое значение предыдущей позиции

        while True:
            line = f.readline()
            if not line:
                break
            elif '.' in line:  # это файл
                line_type = 'file'
            else:  # это папка
                line_type = 'folder'

            line.rstrip()
            level = line.count(' ')  # определяем глубину
            level_difference = level - prev_level  # разница в глубине относительно предыдущей записи

            for _ in range(1 - level_difference):
                path_items_list.pop()  # сокращаем список элементов на количество, рассчитанное по разнице в глубине
            path_items_list.append(line.strip())  # заносим в список текущий элемент
            prev_level = level  # обновляем уровень для следующей итерации

            if line_type == 'folder':
                # создание папки
                os.makedirs(os.path.join(*path_items_list), exist_ok=True)
            else:
                # создание файла
                if not os.path.exists(os.path.join(*path_items_list)):  # если файл еще не создан
                    with open(os.path.join(*path_items_list), 'w'):
                        pass

config_file_name = 'config_2.yaml'
with open(config_file_name) as file:
    dict_structure = yaml.safe_load(file)
pref = ''

def create_project_starter_adv(dict_structure: dict, pref=''):
    for directory, paths in dict_structure.items():
        dir_path = os.path.join(pref, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_project_starter_adv(paths, dir_path)
        else:
            for el in paths:
                if isinstance(el, dict):
                    create_project_starter_adv(el, dir_path)
                elif isinstance(el, str):
                    with open(os.path.join(dir_path, f'{el}'), 'w') as _:
                        pass







if __name__ == '__main__':
    config = 'config_1.yaml'
    create_project_starter(config_file_name=config)

    config = 'config_2.yaml'
    create_project_starter_adv(dict_structure)