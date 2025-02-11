from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_resullt = {}  # Словник для збереження кешу

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print("Getting from cache")
            return cache_resullt[key]  # Повертаємо кешований результат

        print("Calculating new result")
        result = func(*args, **kwargs)  # Обчислюємо новий результат
        cache_resullt[key] = result  # Зберігаємо в кеш
        return result

    return wrapper  # Повертаємо обгорнуту функцію
