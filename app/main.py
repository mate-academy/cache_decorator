from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            return result

    return wrapper


# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> int:
#     return [number ** power for number in n_tuple]
#
#
# print(long_time_func(1, 2, 3))  # Calculating new result
# print(long_time_func(2, 2, 3))  # Calculating new result
# print(long_time_func_2((5, 6, 7), 5))  # Calculating new result
# print(long_time_func(1, 2, 3))  # Getting from cache
# print(long_time_func_2((5, 6, 7), 10))  # Calculating new result
# print(long_time_func_2((5, 6, 7), 10))  # Getting from cache
