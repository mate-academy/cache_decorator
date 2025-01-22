from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        if not all(isinstance(arg, (int, float, str, tuple, bool))
                   for arg in args):
            raise TypeError("Only immutable argument types")
        key = (func.__name__, args)
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        print("Calculating new result")
        cache_storage[key] = func(*args)
        return cache_storage[key]
    return wrapper


@cache
def long_time_func(base: int, exponent: int, multiplier: int) -> int:
    return (base ** exponent ** multiplier) % (base * multiplier)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> Any:
    return [number ** power for number in n_tuple]


if __name__ == "__main__":
    print(long_time_func(1, 2, 3))
    print(long_time_func(2, 2, 3))
    print(long_time_func_2((5, 6, 7), 5))
    print(long_time_func(1, 2, 3))
    print(long_time_func_2((5, 6, 7), 10))
    print(long_time_func_2((5, 6, 7), 10))
