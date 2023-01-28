def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""

    number_100 = number % 100
    number_10 = number_100 % 10
    result_string = f'{number} процент'

    if 5 <= number_100 <= 20:
        result_string += 'ов'
    elif 1 < number_10 < 5:
        result_string += 'a'
    elif number_10 == 1:
        result_string = result_string
    else:
        result_string += 'ов'

    return result_string


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))