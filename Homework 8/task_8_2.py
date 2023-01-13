import re

def check_pattern(filename: str, pattern: str) -> bool:
    """Функция проверяеят каждую строку на наличие шаблона fragment
    Если в каждой строке присутсвует строковый фрагмент, функция вернёт True
    А иначе функция выводит каждую строку текстового файла
    к которой неподошел шаблон fragment """

    with open(filename) as f:
        if all(map(lambda line: bool(re.search(pattern, line)), f.read().splitlines())):
            print(f'Паттерн {pattern} подошёл к каждой строке')
            return True
        f.seek(0)
        for i in list(filter(lambda line: not bool(re.search(pattern, line)), f.read().splitlines())):
            print(i)
        return False

def logs_parse(line: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param line: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_LOGS = re.compile(r'^([(?:\d{,3}\.?){4}|[a-f0-9]*).+(\[.+\])\s(\"[A-Z]+\b)\s(/[a-z]+/[a-z]+_[0-9]+).+\s(\d{3})\s(\d+)')
    check_pattern('nginx_logs.txt', RE_LOGS)
    return RE_LOGS.findall(line)

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

if __name__ == '__main__':
    print(logs_parse(raw))