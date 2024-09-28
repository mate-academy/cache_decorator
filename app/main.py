from typing import Callable, Dict, Tuple, Any
import functools


def cache(func: Callable) -> Callable:
    # Dictionary to store results for different functions
    cache_storage: Dict[str, Dict[Tuple[Any, ...], Any]] = {}

    @functools.wraps(func)
    def wrapper(*args: Tuple[Any, ...]) -> Any:
        func_name = func.__name__

        # Initialize the cache for this function if it doesn't exist
        if func_name not in cache_storage:
            cache_storage[func_name] = {}

        # Check if the arguments are in the cache
        if args in cache_storage[func_name]:
            print("Getting from cache")
            return cache_storage[func_name][args]

        # Calculate the result since it's not in the cache
        print("Calculating new result")
        result = func(*args)

        # Store the result in the cache
        cache_storage[func_name][args] = result
        return result

    return wrapper


# Example functions for testing
@cache
def long_time_func(base: int, exponent: int, modulus: int) -> int:
    return (base ** exponent ** modulus) % (base * modulus)


@cache
def long_time_func_2(text_1: str, text_2: str) -> str:
    return f"{text_1.upper()}, {text_2.lower()}"


@cache
def long_time_func_3(n_list: list, text: str) -> str:
    return f"{[i ** 2 for i in n_list]}, {text}"
