from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    # Store cache per function
    func_cache: dict[tuple, any] = {}

    @wraps(func)
    def wrapper(*args) -> any:
        # Use the arguments as the cache key
        cache_key = args
        if cache_key in func_cache:
            print("Getting from cache")
            return func_cache[cache_key]
        else:
            print("Calculating new result")
            result = func(*args)
            func_cache[cache_key] = result
            return result

    return wrapper


@cache
def long_time_func(number_1: int, number_2: int, number_3: int) -> int:
    return (number_1 ** number_2 ** number_3) % (number_1 * number_3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[any]:
    return [number ** power for number in n_tuple]


# Testing the functions
long_time_func(1, 2, 3)  # Should calculate new result
long_time_func(2, 2, 3)  # Should calculate new result
long_time_func_2((5, 6, 7), 5)  # Should calculate new result
long_time_func(1, 2, 3)  # Should get from cache
long_time_func_2((5, 6, 7), 10)  # Should calculate new result
long_time_func_2((5, 6, 7), 10)  # Should get from cache
