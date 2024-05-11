from typing import Callable


def cache(func: Callable) -> Callable:
    arguments = {}

    def wrapper(*args) -> Callable:
        if args not in arguments and isinstance(args, (int, float, tuple)):
            result = func(*args)
            arguments.update({args: result})
            print("Calculating new result")
            return result
        print("Getting from cache")
        return arguments[args]
    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
