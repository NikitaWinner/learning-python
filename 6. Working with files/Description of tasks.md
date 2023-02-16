

## Задание 
получить данные, как на примере, из файл логов web-сервера https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
вывод должен представлять с собой список кортежей: `(<remote_addr>, <request_type>, <requested_resource>)` . 
Пример Вывода:

```
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
```


Алгоритм должен вычислять IP адрес атаковавшего сервер по данным файла логов.

> Код должен работать даже с файлами, 
> размер которых превышает объем ОЗУ компьютера.



