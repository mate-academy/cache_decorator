from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        try:
            key = (args, frozenset(kwargs.items()))  # Незмінний ключ
        except TypeError:
            raise TypeError("Arguments must be immutable")

        # Якщо ключ вже в кеші
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        # Якщо ключа немає, обчислюємо результат
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper
