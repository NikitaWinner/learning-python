from random import uniform, randint


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""

    for i in range(len(list_in)):
        list_in[i] = str(list_in[i]).split('.')
        list_in[i] = f'{list_in[i][0]} руб {list_in[i][1].ljust(2, "0")} коп'
    str_out = ', '.join(list_in)
    return str_out


print()
my_list = [round(uniform(10, 100), 2) for _ in range(1, 11)]  # автоматическая генерация случайных 10 дробных чисел.
print(f'Исходный список №1: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(f'Преобразованный список №1: {result_1}')


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


print('\n\n')
# зафиксируйте здесь информацию по исходному списку my_list
my_list = [round(uniform(10, 100), 2) for _ in range(1, 11)]
list_before = id(my_list)  # сохранил id списка до сортировки
print(f'Исходный список №2 (id {list_before}) : {my_list}')
result_2 = sort_prices(my_list)
list_after = id(result_2)  # сохранил id списка после сортировки
print(f'Отсортированный по возрастанию список №2 (id {list_after}): {result_2}')

if list_before == list_after:
    print('Список №2 после сортировки неизменился.')
else:
    print('Список №2 после сортировки изменился.')

def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""

    list_out = sorted(list_in, reverse=True)
    return list_out


print('\n\n')
my_list = [round(uniform(10, 100), 2) for _ in range(1, 11)]
list_before = id(my_list)  # сохранил id списка до сортировки
print(f'Исходный список №3 (id {list_before}): {my_list}')
result_3 = sort_price_adv(my_list)
list_after = id(result_3)  # сохранил id списка после сортировки
print(f'Отсортированный по убыванию список №3 (id {list_after}): {result_3}')

if list_before == list_after:
    print('Список №3 после сортировки неизменился.')
else:
    print('Список №3 после сортировки изменился.')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = sorted(list_in, reverse=True)[:5]
    return list_out


print('\n\n')
my_list = [round(uniform(10, 100), 2) for _ in range(1, randint(11, 11))]
print(f'Исходный список №4: {my_list}')
result_4 = check_five_max_elements(my_list)
print(f'5 максимальных значений списка №4: {result_4}')