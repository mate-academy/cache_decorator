from typing import Callable
from functools import wraps


cache_storage = {}


def cache(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        # Перевірка, чи аргументи є незмінними
        if not all(isinstance(arg, (int, float, str, tuple)) for arg in args):
            raise TypeError(
                "Cache decorator works only with immutable arguments")

        # Формуємо ключ для кешу
        cache_key = (func, args)

        # Перевіряємо наявність у кеші
        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[cache_key] = result
            return result
    return wrapper
