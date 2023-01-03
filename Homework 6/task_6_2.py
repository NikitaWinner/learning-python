import collections
from create_file import get_file_nginx, NGINX_FILE


def find_spam(file: str) -> tuple:
    """Функция находит наибольшее количество повторений IP-адреса среди логов
    :param file: строка с логами"""

    list_ip = []
    dict_ip = {}
    for line in file.splitlines():
        ip = line.split()[0]
        list_ip.append(ip)
        dict_ip[ip] = 0
    for key in list_ip:
        dict_ip[key] += 1

    max_amount = max(dict_ip.values())
    spammer_ip = ''.join([key for key in dict_ip if dict_ip[key] == max_amount])
    return spammer_ip, max_amount


def find_spam_adv(file: str) -> tuple:
    """Функция находит наибольшее количество повторений IP-адреса среди логов
    :param file: строка с логами"""

    dict_ip = collections.Counter()
    for line in file.splitlines():
        ip_address = line.split()[0]
        dict_ip[ip_address] += 1
    max_amount = dict_ip.most_common(1)[0][1]
    spammer_ip = dict_ip.most_common(1)[0][0]
    return spammer_ip, max_amount


def find_spam_adv_2(file: str) -> tuple:
    """Функция находит наибольшее количество повторений IP-адреса среди логов
    :param file: строка с логами"""

    with open(NGINX_FILE) as file:
        dict_ip = {}
        spammer_ip = None
        max_amount = 0
        while True:
            line = file.readline()
            if not line:
                break
            ip_address = line.strip().split()[0]
            if ip_address in dict_ip:
                dict_ip[ip_address] += 1
            else:
                dict_ip[ip_address] = 1
            if max_amount < dict_ip[ip_address]:
                max_amount = dict_ip[ip_address]
                spammer_ip = ip_address
    return spammer_ip, max_amount



logs = get_file_nginx(NGINX_FILE)

spammer_ip, amount_requests = find_spam(logs)
print(f'IP спамера -> {spammer_ip} \nКол-во запросов -> {amount_requests}')

spammer_ip_adv, amount_requests_adv = find_spam_adv(logs)
print(f'IP спамера -> {spammer_ip_adv} \nКол-во запросов -> {amount_requests_adv}')

spammer_ip_adv_2, amount_requests_adv_2 = find_spam_adv_2(logs)
print(f'IP спамера -> {spammer_ip_adv_2} \nКол-во запросов -> {amount_requests_adv_2}')




