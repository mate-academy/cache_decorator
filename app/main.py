from functools import wraps
from typing import Callable, Any


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    """Декоратор для кешування результатів функції з незмінними аргументами."""
    cache_storage: dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        print("Calculating new result")
        result = func(*args)
        cache_storage[args] = result
        return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, coefficient: int) -> int:
    """Обчислення виразу з трьома аргументами."""
    return (base ** exponent ** coefficient) % (base * coefficient)


@cache
def long_time_func_2(numbers_tuple: tuple[int, ...], power: int) -> list[int]:
    """Обчислення степеня для кожного числа у кортежі."""
    return [number ** power for number in numbers_tuple]


# Виклики функцій для перевірки роботи кеша
long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
