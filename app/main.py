from typing import Callable


def cache(func: Callable) -> Callable:
    # Словник для зберігання результатів, - наш Кеш,
    # де ключі це аргументи, а значення результат функції
    cache_dict = {}

    def wrapper(*args):
        # Якщо аргументи вже є в кеші, повертаємо збережений результат
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            # Якщо аргументів немає в кеші, обчислюємо новий результат
            # та зберігаємо його в наш кеш
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
            return result

    return wrapper
