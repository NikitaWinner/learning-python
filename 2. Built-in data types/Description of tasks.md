# Урок 2. Некоторые встроенные типы и операции с ними
## Задание 1
Выяснить тип результата выражений:

```
15 * 3
15 / 3
15 // 2
15 ** 2
```

## Задание 2
На вход будет выдаваться список, пример:

```
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
```

a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём 
до двух целочисленных разрядов:

```
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
```

b) Сформировать из обработанного списка строку:

`в "05" часов "17" минут температура воздуха была "+05" градусов`

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
Как модифицировать это условие для чисел со знаком?

> Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. 
> Главное: дополнить числа до двух разрядов нулём!


## Задание 3
*(вместо задачи 2) Решить задачу 2, не создавая новый список (как говорят, in place). 
Эта задача намного серьёзнее, чем может сначала показаться.

## Задание 4
На вход будет подаваться список, содержащий искажённые данные с должностями и именами сотрудников:

```
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
```

Известно, что имя сотрудника всегда в конце строки! 

Обработать все элементы списка и вернуть в качестве результата список, состоящий из фраз вида:

```
['Привет, Игорь!', 'Привет, Марина!', 'Привет, Николай!', 'Привет, Аэлита!']
```

Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. 

Можно ли при этом не создавать новый список?


## Задание 5
Создать вручную список, содержащий цены на товары (10–20 товаров), например:

```
[57.8, 46.51, 97, ...]
```

a) Привести каждый элемент списка к виду `<r> руб <kk> коп` и собрать их в одну строку через запятую. 
Пример: 

```
57 руб 80 коп, 46 руб 51 коп ...
```

Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 
`7 копеек` или `0 копеек` (должно быть `07 коп` или `00 коп`).

b) Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что 
объект списка после сортировки остался тот же).

c) Создать новый список, содержащий те же цены, но отсортированные по убыванию.

d) Вернуть цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по 
возрастанию, написав минимум кода?

> Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
