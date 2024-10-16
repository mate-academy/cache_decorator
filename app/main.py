from typing import Callable
from functools import wraps
import logging


# Configure logging with INFO level
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        if args in cache_storage:
            logging.info("Getting from cache: %s", args)
            return cache_storage[args]
        else:
            logging.info("Calculating new result for: %s", args)
            result = func(*args)
            cache_storage[args] = result
            return result
    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
