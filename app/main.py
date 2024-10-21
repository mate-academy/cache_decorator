from typing import Callable, Any, Hashable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args: Hashable, **kwargs: Hashable) -> Any:
        cache_key = (args, tuple(kwargs.items()))
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result
    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
