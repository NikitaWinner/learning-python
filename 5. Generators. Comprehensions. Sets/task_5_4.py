import typing


def get_numbers_1(src: list) -> list:
    """ Функция возвращает список, в котором остаются только те элементы,
    которые больше предыдущего в переданном списке """

    return [src[i+1] for i in range(len(src)-1) if src[i] < src[i+1]]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers_1(src))

def get_numbers_2(src: list) -> typing.Generator:
    """ Функция возвращает генератор, который отдаёт те элементы,
    которые больше предыдущего в переданном списке """

    return (val for indx, val in enumerate(src) if src[indx - 1] < src[indx] and indx > 0)


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers_2(src))