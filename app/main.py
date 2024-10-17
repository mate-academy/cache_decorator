from typing import Callable, Any, Tuple
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
