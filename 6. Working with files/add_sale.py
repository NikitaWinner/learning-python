import os
import sys
from create_file import NAMES_BAKERY_FILE


def help():
    print('\nCommands:')
    print('  help                   Show help for commands.')
    print('  all                    Show all available files.\n')
    print('General Options:')
    print('  [filename]             Select this file to write data')
    print('  -с                     The specified key creates a csv-format file with this name')
    print('  [data]                 The specified data is written to a file\n')
    print('Use case:')
    print('  bakery -c              Сreating a file named "bakery.csv"')
    print('  bakery 4567,8 -c       Сreating a file named "bakery.csv" and writing data "4567,8" to this file')
    print('  bakery 4567,8          Open file named "bakery.csv" and write data "4567,8" to this file\n')


def print_file():
    """Функция считывает текстовый фаил с именами файлов и их выводит на экран
    :return: None"""
    with open(NAMES_BAKERY_FILE, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            print(line.strip())
            count += 1
        if count == 0:
            print('\n No files available :( \n')
        print(f'\nAmount of files: {count}\n')

def create_file_csv(filename):
    """Функция проверяет наличие создаёт csv-фаил
    :param filename:
    :return:
    """
    if not check_file(filename):
        path_to_file = os.path.join("data_file", filename)
        with open(f'{path_to_file}.txt', 'w', encoding='utf-8') as file:
            with open(NAMES_BAKERY_FILE, 'a', encoding='utf-8') as file_2:
                file_2.write(f'{filename}\n')
        print(f'\nDone! File named "{filename}" created.\n')
    else:
        print(f'\nFile named "{filename}" already exists.\n')


def check_file(name):
    """Проверяет наличие файлов по имени из текстового файла с именами"""
    with open(NAMES_BAKERY_FILE, 'a+', encoding='utf-8') as file:
        file.seek(0)
        for line in file:
            if name == line.strip():
                return True
        return False


def write_data(filename, data, create=False):
    """Записывает данные в файл проверяя существования файла,
     если файла не существует, то созаёт его и записывает туда данные"""
    if create:
        if not check_file(filename):
            create_file_csv(filename)
            path_to_file = os.path.join('data_file', filename)
            with open(f'{path_to_file}.txt', 'a', encoding='utf-8') as file:
                file.write(f'{data}\n')
                print(f'\nReady. Data "{data}" written to file\n')
        else:
            print(f'\nFile named "{filename}" already exists.\n')
    else:
        if check_file(filename):
            path_to_file = os.path.join('data_file', filename)
            with open(f'{path_to_file}.txt', 'a', encoding='utf-8') as file:
                file.write(f'{data}\n')
                print(f'\nReady. Data "{data}" written to file\n')
        else:
            print('\nFile with this name does not exist\n')

if __name__ == '__main__':
    arg = sys.argv
    if arg[1] == 'help':
        help()
    elif arg[1] == 'all':
        print_file()
    elif '-c' not in arg:
        write_data(arg[1], arg[2])
    elif arg[2] == '-c':
        create_file_csv(arg[1])
    elif arg[3] == '-c':
        write_data(arg[1], arg[2], create=True)
    else:
        print('The command is entered incorrectly or there is no such command')




