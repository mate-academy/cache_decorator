from typing import Callable, Any, Tuple, List
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache_store:
            print('Getting from cache')
            return cache_store[args]
        else:
            print('Calculating new result')
            result = func(*args)
            cache_store[args] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulo: int) -> int:
    return (base ** exponent ** modulo) % (base * modulo)


@cache
def long_time_func_2(n_tuple: Tuple[int, ...], power: int) -> List[int]:
    return [number ** power for number in n_tuple]
