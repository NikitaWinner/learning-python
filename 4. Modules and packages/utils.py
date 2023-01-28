import requests
from datetime import date

def currency_rates_adv(code: str):
    """возвращает курс валюты `code` по отношению к рублю с датой"""

    data = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    data = data.text.split('<Valute ID=')
    day, month, year = map(int, data[0].split('"')[5].split('.'))
    time = date(year=year, month=month, day=day)
    val = None
    for elem in data:
        if code.upper() in elem:
            val = round(float(elem.replace('/', '').split('<Value>')[-2].replace(',', '.')), 2)
    return val, time

