from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    cache_dict: Dict[str, Dict[Tuple, Any]] = {}  # Общий кэш для всех функций

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        # Создаем отдельный кэш для каждой функции
        if func.__name__ not in cache_dict:
            cache_dict[func.__name__] = {}

        # Проверяем, есть ли результат в кэше для текущих аргументов
        if key not in cache_dict[func.__name__]:
            print("Calculating new result")
            cache_dict[func.__name__][key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_dict[func.__name__][key]

    return wrapper