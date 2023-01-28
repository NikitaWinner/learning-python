from functools import wraps


def val_checker(validator=lambda val: isinstance(val, int) and val >= 0):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                if not all(map(validator, args)):
                    msg = f'wrong val {args}'
                    raise ValueError(msg)
            return func(*args, **kwargs)
        return wrapper
    return _val_checker

# def validator(val) -> bool:
#     """Функция проверки переданного значения (положительное целое число или 0)"""
#     return isinstance(val, int) and val >= 0

@val_checker()
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
