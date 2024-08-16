from typing import Callable, Any, Dict, Tuple
from functools import wraps


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_dict: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent ** modulus) % (base * modulus)


@cache
def long_time_func_2(numbers: tuple, power: int) -> list:
    return [number ** power for number in numbers]
