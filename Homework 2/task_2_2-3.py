def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""

    for i in range(len(list_in)):
        if list_in[i][0] in '+-':
            list_in[i] = f'"{list_in[i].zfill(3)}"'
        elif list_in[i].isdigit():
            list_in[i] = f'"{list_in[i].zfill(2)}"'
    str_out = ' '.join(list_in)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)