from typing import Callable, Any, Tuple
import functools


def cache(func: Callable) -> Callable:
    # Dictionary to hold cache for each function
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
        # Create a key based on the function name and arguments
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
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent) % (base * modulus)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
