import os
import sys
from add_sale import check_file


def show_sale(arg_tuple):
    """Функция считывает текстовый фаил с именами файлов и их выводит на экран
    :return: None"""
    try:
        if check_file(arg_tuple[1]):
            path_to_file = os.path.join('data_file', arg_tuple[1])
            with open(f'{path_to_file}.txt', 'r', encoding='utf-8') as file:
                if len(arg_tuple) == 2:
                    for line in file:
                        print(line.strip())
                elif len(arg_tuple) == 3:
                    count = 0
                    for line in file:
                        count += 1
                        if count >= int(arg_tuple[2]):
                            print(line.strip())
                elif len(arg_tuple) == 4:
                    count = 0
                    for line in file.readlines()[int(arg_tuple[2])-1:int(arg_tuple[3])]:
                        print(line.strip())
    except IndexError:
        print('\nEnter the name of the file you want to view\n')



arg = sys.argv
show_sale(arg)
