def get_uniq_numbers(src: list):
    """ Функция возвращает генератор, отдающий элементы,
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
print(*get_uniq_numbers(src))