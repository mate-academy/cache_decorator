from functools import wraps
from typing import Callable, Tuple, Any


def cache(func: Callable) -> Callable:
    func_cache = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            func_cache[args] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, multiplier: int) -> int:
    return (base ** exponent ** multiplier) % (base * multiplier)


@cache
def long_time_func_2(numbers: Tuple[int, ...], power: int) -> list[int]:
    return [number ** power for number in numbers]
