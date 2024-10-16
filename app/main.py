from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}  # Dictionary to store results of completed runs

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            return result
    return wrapper

# Example usage


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]


# Test the cache decorator


long_time_func(1, 2, 3)          # Calculating new result
long_time_func(2, 2, 3)          # Calculating new result
long_time_func_2((5, 6, 7), 5)   # Calculating new result
long_time_func(1, 2, 3)          # Getting from cache
long_time_func_2((5, 6, 7), 10)   # Calculating new result
long_time_func_2((5, 6, 7), 10)   # Getting from cache
