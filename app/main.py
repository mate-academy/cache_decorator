from typing import Callable, Tuple, List, Any


def cache(func: Callable) -> Callable:
    d_cache: dict[Tuple[Any, frozenset], Any] = {}  # Типізуємо словник-кеш

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, frozenset(kwargs.items()))  # Створюємо ключ із аргументів

        if cache_key in d_cache:
            print("Getting from cache")
            return d_cache[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        d_cache[cache_key] = result  # Зберігаємо новий результат у кеші
        return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: Tuple[int, ...], power: int) -> List[int]:
    return [number ** power for number in n_tuple]


# Виклики функцій для перевірки
long_time_func(1, 2, 3)  # Має вивести "Calculating new result"
long_time_func(2, 2, 3)  # Має вивести "Calculating new result"
long_time_func_2((5, 6, 7), 5)  # Має вивести "Calculating new result"
long_time_func(1, 2, 3)  # Має вивести "Getting from cache"
long_time_func_2((5, 6, 7), 10)  # Має вивести "Calculating new result"
long_time_func_2((5, 6, 7), 10)  # Має вивести "Getting from cache"
