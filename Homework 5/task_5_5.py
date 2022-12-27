import typing

def get_uniq_numbers_1(src: list) -> list:
    """ Функция возвращает список, отдающий элементы,
    которые не имеют повторений в переданном списке
    :param src: список со значениями
    :return: генератор с уникальными значениями """

    temp = set()
    set_out = set()
    for elem in src:
        if elem not in temp:
            set_out.add(elem)
        else:
            set_out.discard(elem)
        temp.add(elem)
    return [el for el in src if el in set_out]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers_1(src))


def get_uniq_numbers_2(src: list) -> typing.Generator:
    """ Функция возвращает генератор, который отдаёт те элементы,
    которые больше предыдущего в переданном списке
    :param src: список со значениями
    :return: генератор с уникальными значениями """

    dict_temp = {key: 0 for key in src}
    for key in src:
        dict_temp[key] += 1
    return (key for key in dict_temp if dict_temp[key] == 1)


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers_2(src))
