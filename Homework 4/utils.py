import datetime
import requests


def return_index(string: str, char_code: str, entry='first') -> int:
    """
    Функция принимает строку и подстроку возвращает индекс первого
    или последнего вхождения подстроки char_code в строку string
    в зависимости от установленого флага edge
    :param string: строка, в которой будет проводиться поиск индекса
    :param char_code: подстрока, индекс которой будет возвращаться
    :param entry: флаг, который определяет индекс первого или последнего
    вхождения будет возвращен. Если start - первое вхождение
                               Если end -  последнее вхождение (indx + 1)
    :return: индекс подстроки
    """

    if entry == 'first':
        return int(string.find(char_code))
    elif entry == 'last':
        return int(string.find(char_code)) + len(char_code) - 1
    else:
        pass


def currency_rates_adv(code: str):
    """возвращает курс валюты `code` по отношению к рублю"""
    programm, code = code
    data = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    data = data.text.split('ID')
    print(len(data))
    index_start = return_index(data[0], 'Date="', entry='last') + 1
    index_end = return_index(data[0], '" name="', entry='first')
    time = data[0][index_start:index_end]
    time_obj = datetime.datetime.strptime(time, '%d.%m.%Y')
    dict_out = {}
    del data[0]
    for element in data:
        index_start = return_index(element, '<CharCode>', entry='last') + 1
        index_end = return_index(element, '</CharCode>', entry='first')
        char_code = element[index_start:index_end]
        index_start = return_index(element, '<Value>', entry='last') + 1
        index_end = return_index(element, '</Value>', entry='first')
        value = float(element[index_start:index_end].replace(',', '.'))
        index_start = return_index(element, '<Nominal>', entry='last') + 1
        index_end = return_index(element, '</Nominal>', entry='first')
        nominal = float(element[index_start:index_end])
        dict_out[char_code] = round(value / nominal, 2)
    return dict_out.get(code.upper()), time_obj



