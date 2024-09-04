from functools import wraps
from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    results: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> [int, list]:
        key = (args, frozenset(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            result = func(*args, **kwargs)
            results[key] = result
            print("Calculating new result")
            return result

    return wrapper


@cache
def long_time_func(ab: int, bc: int, cd: int) -> int:
    return (ab ** bc ** cd) % (ab * cd)


@cache
def long_time_func_2(n_tuple: Tuple[int, int, int], power: int) -> list:
    return [number ** power for number in n_tuple]
