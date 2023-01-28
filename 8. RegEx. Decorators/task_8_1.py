import re
import random
import string


def generate_email_address(count: int) -> list[str]:
    """
    Функция генерирует поддельные е-мейл адреса в кол-ве count
    :param count: количество адресов, которое нужно сгенерировать
    :return: список строк, каждая строка это емеил адрес
    """
    symbol = '-_.' + string.ascii_letters + string.digits
    mail_random_list = []
    mail_server_list = ['gmail.com', 'yandex.ru', 'outlook.com', 'mail.ru', 'yahoo.com']
    for i in range(count):
        random_mail = random.sample(symbol, random.randrange(1, 12))
        random_mail = ''.join(random_mail)
        random_mail_server = mail_server_list[random.randrange(0, len(mail_server_list))]
        mail_random_list.append(f'{random_mail}@{random_mail_server}')
    return mail_random_list


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'[\w\-\.]+@[\w\-\.]+\.\w+')
    if not RE_MAIL.match(email):
        msg = f'wrong email: {email}'
        raise ValueError(msg)
    keys = ['username', 'domain']
    values = email.split('@')
    return {keys[i]: values[i] for i in range(2)}


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'), '\n')
    rand_email = generate_email_address(100)
    for email in rand_email:
        print(email_parse(email))
    print(email_parse('someone@geekbrainsru'))