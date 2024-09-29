from typing import Callable, Dict, Tuple, Any
import functools


def cache(func: Callable) -> Callable:
    cache_storage: Dict[Any, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = (func.__name__, args, kwargs_tuple)

        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        cache_storage[cache_key] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent ** modulus) % (base * modulus)


@cache
def long_time_func_2(text_1: str, text_2: str) -> str:
    return f"{text_1.upper()}, {text_2.lower()}"


@cache
def long_time_func_3(n_list: list, text: str) -> str:
    return f"{[i ** 2 for i in n_list]}, {text}"
