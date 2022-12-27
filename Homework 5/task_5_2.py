import typing


def odd_nums(number: int) -> typing.Generator:
    """ Генератор, возвращающий по очереди нечетные целые числа
     от 1 до number (включительно), без использования оператора yield """

    return (_ for _ in range(1, number + 1, 2))


n = 15
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))

print(f'Тип объекта generator -> {type(generator)}')
#  next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
