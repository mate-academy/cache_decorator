from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args) -> Any:
        # Ініціалізуємо кеш, якщо він не існує як атрибут wrapper
        if not hasattr(wrapper, "_cache"):
            wrapper._cache = {}

        # Перевіряємо, чи є результат для цих аргументів у кеші
        if args in wrapper._cache:
            print("Getting from cache")
            return wrapper._cache[args]
        else:
            print("Calculating new result")
            # Обчислюємо та зберігаємо результат, якщо його немає в кеші
            result = func(*args)
            wrapper._cache[args] = result
            return result
    return wrapper
