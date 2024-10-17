from functools import wraps
from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:

    cache_storage = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        cache_key = (func.__name__, args)

        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[cache_key] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent) % (base * modulus)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
