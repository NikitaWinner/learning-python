def print_type_object(*objects):
    """Выводит в консоль типы переданых объектов в параметр objects"""

    for object in objects:
        print(f'Тип объекта: {object} -> {object.__class__.__name__}')

print_type_object(15 * 3, 15 / 3, 15 // 2, 15 ** 3, 'hello', bool(1), [], ())
