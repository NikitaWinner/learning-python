import os
import sys
from add_sale import check_file


def change(arg_tuple):
    if check_file(arg_tuple[1]):
        path_to_file = os.path.join('data_file', arg_tuple[1])
        line_list = []
        with open(f'{path_to_file}.txt', 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                line_list.append(line)
        if len(line_list) >= int(arg_tuple[2]):
            replacement = line_list[int(arg_tuple[2])-1]
            line_list[int(arg_tuple[2])-1] = arg_tuple[3]+'\n'
            with open(f'{path_to_file}.txt', 'w', encoding='utf-8') as file:
                for line in line_list:
                    file.write(line)
                print(f'\nIn the "{arg_tuple[1]}" file, line №{arg_tuple[2]} changed the value "{replacement}" to "{arg_tuple[3]}".\n')
        else:
            print('\nThere is no entry in the file with the received number.\n')

arg = sys.argv
change(arg)