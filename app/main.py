from typing import Callable, Any, Tuple, Dict


def cache(func: Callable) -> Callable:
    cache_storage: Dict[Tuple, Any] = {}

    def wrapper(*args) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]

        print("Calculating new result")
        cache_storage[args] = func(*args)
        return cache_storage[args]

    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
