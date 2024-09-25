from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    return wrapper


@cache
def long_time_func(base: int, exponent: int, modules: int) -> int:
    return (base ** exponent ** modules) % (base * modules)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
