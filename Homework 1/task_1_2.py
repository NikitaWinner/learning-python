def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""

    sum_number = 0
    for number in dataset:
        sum_digit = 0
        for digit in str(number):
            sum_digit += int(digit)
        else:
            if sum_digit % 7 == 0:
                sum_number += number

    return sum_number  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""

    for i in range(len(dataset)):
        dataset[i] += 17

    return sum_list_1(dataset)  # Верните значение полученной суммы

def sum_list_3(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""

    sum_number = 0
    for number in dataset:
        number += 17
        sum_digit = 0
        num_saved = number
        while number != 0:
            sum_digit += number % 10
            number //= 10
        if sum_digit % 7 == 0:
            sum_number += num_saved

    return sum_number

my_list = [number ** 3 for number in range(1, 1001, 2)]  # Соберите нужный список по заданию

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)

my_list = [number ** 3 for number in range(1, 1001, 2)]

result_3 = sum_list_3(my_list)
print(result_3)


