# Урок 8. Регулярные выражения и декораторы в Python

## Задание 1
Написать тело функцию `email_parse(email: str)`, которая при помощи регулярного выражения извлекает имя 
пользователя и почтовый домен из email адреса и возвращает их в виде словаря. 
Если адрес не валиден, выбросить исключение `ValueError`. Пример:

```
$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
$ email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
```

> Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); 
> как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; 
> можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?


## Задание 2 *(вместо 1)
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока 
[`nginx_logs.txt`](https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
 для получения информации вида: 
`(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)`, например:

```
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
```

> Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? 
> Можно ли для них уточнить регулярное выражение?

## Задание 3
Написать декоратор для логирования типов позиционных аргументов функции, например:

```
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3


$ a = calc_cube(5)
5: <class 'int'>
```

> Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип 
> значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? 
> Сможете ли вывести имя функции, например, в виде:

```
$ a = calc_cube(5)
calc_cube(5: <class 'int'>)
```

## Задание 4
Написать декоратор с аргументом-функцией (`callback`), позволяющий валидировать входные значения функции и выбрасывать 
исключение `ValueError`, если что-то не так, например:

```
$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
```

Исключение должно возбуждаться, если значение анализируемого аргумента не является **положительным целочисленным** 
значением, включая 0.

> Примечание: сможете ли вы замаскировать работу декоратора?


> Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
