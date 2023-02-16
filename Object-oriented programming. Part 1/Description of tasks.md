# Урок 9. Объектно-ориентированное программирование. Введение

## Задание 1
Создать класс `TrafficLight` (светофор):
* определить у него один атрибут `color` (цвет) и метод `running` (запуск);
* атрибут реализовать как приватный;
* в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
* продолжительность первого состояния (`red`) составляет `4 секунды`, второго (`yellow`) — `2 секунды`, 
  третьего (`green`) — `3 секунды`;
* переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный) и 
  в `stdout` каждый цвет должен принтоваться ТОЛЬКО ОДИН раз в момент переключения с указанием исходного 
  кол-ва секунд, т.е. формат строки вывода `<текущий цвет> <значение секунд> сек`;
* проверить работу примера, создав экземпляр и вызвав описанный метод.

Пример, `stdout` при обращении к методу `running`:

```
$ traffic = TrafficLight()
$ traffic.running()
red 4 сек
yellow 2 сек
green 3 сек
```

> Задачу можно усложнить, реализовав проверку порядка режимов.
> При его нарушении выводить соответствующее сообщение и завершать скрипт.


## Задание 2
Реализовать класс `Road` (дорога).
* определить атрибуты: `length` (длина), `width` (ширина);
* значения атрибутов должны передаваться при создании экземпляра класса;
* атрибуты сделать `защищёнными`;
* определить метод `calculate` расчёта массы асфальта, необходимого для покрытия всей дороги;
* использовать формулу: 
  `длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * 
  число см толщины полотна`;
* проверить работу метода.
 
Например: `20 м * 5000 м * 25 кг * 5 см = 12500 т.`

> Проверьте! Результат должен получаться в тоннах.


## Задание 3
Реализовать базовый класс `Worker` (работник):
* определить атрибуты: `name`, `surname`, `position` (должность), `income` (доход);
* последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», 
  например, `{"wage": wage, "bonus": bonus}`;
* создать класс `Position` (должность) на базе класса `Worker`;
* в классе `Position` реализовать методы получения полного имени сотрудника (`get_full_name`) и дохода с 
  учётом премии (`get_total_income`);
* проверить работу примера на реальных данных: создать экземпляры класса `Position`, передать данные, 
  проверить значения атрибутов, вызвать методы экземпляров.


## Задание 4
Реализуйте базовый класс `Car`:
* у класса должны быть следующие атрибуты: `speed`, `color`, `name`, `is_police` (булево). 
  А также методы: `go`, `stop`, `turn(direction)`, которые должны сообщать в stdout информацию по формату
  (формат сообщений смотрите в документации методов исходного задания);
* значение аргумента `direction`, передаваемого в метод `turn(direction)` может иметь только одно из 
  четырез значений: `направо`, `налево`, `прямо` или `назад` (если передать другое значение, то должно быть 
  возбуждено исключение `ValueError` с сообщением `нераспознанное направление движения`)
* опишите несколько дочерних классов: `TownCar`, `SportCar`, `WorkCar`, `PoliceCar`;
* добавьте в базовый класс метод `show_speed`, который должен показывать текущую скорость автомобиля 
  по формату в документации метода, если атрибут `is_police` равен `True`, то при вызове метода выводить 
  в `stdout` дополнительно второе сообщение `Вруби мигалку и забудь про скорость!`;
* для классов `TownCar` и `WorkCar` переопределите метод `show_speed`. 
  При значении скорости свыше `60 (TownCar)` и `40 (WorkCar)` в `stdout` должно выводиться сообщение о 
  превышении скорости `Alarm!!! Speed!!!`, если превышения нет, то стандартное сообщение из родительского класса.
 
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.


## Задание 5
Реализовать класс `Stationery` (канцелярская принадлежность):
* определить в нём атрибут `title` (название) и метод `draw` (отрисовка). Метод выводит сообщение `Запуск отрисовки`;
* создать три дочерних класса `Pen` (ручка), `Pencil` (карандаш), `Handle` (маркер);
* реализовать переопределение метода `draw` таким образом, чтобы для каждого класса метод 
  выводил в `stdout` только сообщение формата `<Имя класса>: приступил к отрисовке объекта "<title>"`, при этом 
  для класса `Pencil` при запуске метода `draw` в `stdout` сначала выводить сообщение `Запуск отрисовки`, а потом 
  своё уникальное по формату;
* создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
