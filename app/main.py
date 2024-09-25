from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args) -> None:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_data[args] = result
            return result

    return wrapper


@cache
def long_time_func(num_a: int, num_b: int, num_c: int) -> int:
    return (num_a ** num_b ** num_c) % (num_a * num_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


print(long_time_func(1, 2, 3))
print(long_time_func(2, 2, 3))
print(long_time_func_2((5, 6, 7), 5))
print(long_time_func(1, 2, 3))
print(long_time_func_2((5, 6, 7), 10))
print(long_time_func_2((5, 6, 7), 10))
