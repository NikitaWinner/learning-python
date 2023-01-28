from create_file import get_file_nginx, NGINX_FILE
from pprint import pprint

def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов
    (<remote_addr>, <request_type>, <requested_resource>)"""
    line = line.split()
    ip, get, url = line[0], line[5][1:], line[6]
    return ip, get, url


def get_list_logs(file: str) -> list:
    return [get_parse_attrs(line) for line in file.splitlines()]


file = get_file_nginx(NGINX_FILE)
list_out = get_list_logs(file)
pprint(list_out)

