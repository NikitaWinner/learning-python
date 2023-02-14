

## Задание 
(https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7)
(получить определённые данные) файл логов web-сервера [nginx_logs.txt](https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
— получить список кортежей вида: `(<remote_addr>, <request_type>, <requested_resource>)` . 
Например:

```
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
```


Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

> спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, 
> размер которых превышает объем ОЗУ компьютера.



