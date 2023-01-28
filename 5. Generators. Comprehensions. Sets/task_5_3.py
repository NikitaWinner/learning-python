import typing
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Вася', 'Егор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']


def check_gen_1(tutors: list, klasses: list) -> typing.Generator:
    """ Функция возвращает генератор, который отдаёт
    элементы ввиде кортежей (<tutors>, <klasses>) """
    if len(tutors) > len(klasses):
        for i in range(len(tutors) - len(klasses)):
            klasses.append(None)
    else:
        klasses = klasses[:len(tutors)]
    for i in range(len(tutors)):
        yield tutors[i], klasses[i]


generator = check_gen_1(tutors, klasses)
print(f'Тип возвращаемого значения функции check_gen_1 -> {type(generator)}')
# for _ in range(len(tutors)):
#     print(next(generator))
# next(generator)  # если раскомментировать, то в traceback упадёт исключение StopIteration

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Вася', 'Егор']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']


def check_gen_2(tutors: list, klasses: list) -> typing.Generator:
    """ Функция возвращает генератор, который отдаёт
     элементы ввиде кортежей (<tutors>, <klasses>) """

    for i in range(len(tutors)):
        yield tutors[i], klasses[i] if i < len(klasses) else None


generator = check_gen_2(tutors, klasses)
print(f'Тип возвращаемого значения функции check_gen_2 -> {type(generator)}')
# for _ in range(len(tutors)):
#     print(next(generator))
# next(generator)  # если раскомментировать, то в traceback упадёт исключение StopIteration

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Вася', 'Егор']
klasses = ['9А', '7В', '6А', '7В', '9Б', '9В', '8Б', '10А', '10Б']


def check_gen_3(tutors: list, klasses: list) -> typing.Generator:
    """ Функция возвращает генератор, который отдаёт
     элементы ввиде кортежей (<tutors>, <klasses>) """

    return (_ for _ in zip_longest(tutors, klasses))

# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration


generator = check_gen_3(tutors, klasses)
print(f'Тип возвращаемого значения функции check_gen_3 -> {type(generator)}')
# for _ in range(len(tutors)):
#     print(next(generator))
# next(generator)  # если раскомментировать, то в traceback упадёт исключение StopIteration