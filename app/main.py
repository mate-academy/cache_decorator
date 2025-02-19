from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cached_result = {}

    @functools.wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key_tuple = (args, frozenset(kwargs.items()))

        if key_tuple in cached_result:
            print("Getting from cache")
            return cached_result[key_tuple]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_result[key_tuple] = result
        return result

    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[Any]:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)