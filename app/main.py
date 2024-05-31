from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    cache_storage: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args: Any) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, mod_value: int) -> int:
    return (base ** exponent ** mod_value) % (base * mod_value)


@cache
def long_time_func_2(numbers_tuple: Tuple[int, ...], power: int) -> int:
    return [number ** power for number in numbers_tuple]
