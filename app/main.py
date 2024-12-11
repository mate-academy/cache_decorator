from typing import Callable, Tuple, List
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        key = tuple(args)
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]

        print("Calculating new result")
        result = func(*args)
        cache_store[key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent1: int, exponent2: int) -> int:
    return (base ** exponent1 ** exponent2) % (base * exponent2)


@cache
def long_time_func_2(number_tuple: Tuple[int, ...], power: int) -> List[int]:
    return [number ** power for number in number_tuple]
