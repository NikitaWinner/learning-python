from functools import wraps


def type_logger(func):
    @wraps(func)
    def logger(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'name func: {func.__name__}')
        if args:
            type_args_str = ', '.join([f'{arg}: {type(arg)}' for arg in args])
            print(f'positional arg: ({type_args_str})')
        if kwargs:
            type_kwargs_str = ', '.join([f'{key}: {type(val)}' for key, val in kwargs.items()])
            print(f'keyword arg: ({type_kwargs_str})')
        return res

    return logger

@type_logger
def calc_cube(x, *args, **kwargs):
   return x ** 3

if __name__ == '__main__':
    a = calc_cube(5, 'Hi', True, 5.5, my_dict={}, my_list=[])
    print(a)
    print(calc_cube.__name__)
