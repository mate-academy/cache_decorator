from functools import wraps
from typing import Callable, Any, Tuple


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args: Tuple[Any, ...]) -> Any:
        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result

    return wrapper


@cache
def long_time_func(exp1: int, exp2: int, exp3: int) -> None:
    return (exp1 ** exp2 ** exp3) % (exp1 * exp3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> Any:
    return [number ** power for number in n_tuple]
