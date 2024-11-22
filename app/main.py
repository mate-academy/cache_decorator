from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> None:
        cache_key = (args, tuple(kwargs.items()))
        # Створюємо унікальний ключ для кешу з args та kwargs
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        else:
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            print("Calculating new result")
            return result  # Потрібно повертати результат функції

    return inner
