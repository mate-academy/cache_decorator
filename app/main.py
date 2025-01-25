from typing import Callable, List, Any
import functools


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result
    return wrapper


@cache
def long_time_func(base: int, exponent: int, mod: int) -> int:
    return (base ** exponent ** mod) % (base * mod)


@cache
def long_time_func_2(numbers: tuple, power: int) -> List[int]:
    return [number ** power for number in numbers]
