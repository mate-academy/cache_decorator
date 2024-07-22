from typing import Callable, List


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Callable) -> object:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]

        print("Calculating new result")
        result = func(*args)
        cache_storage[args] = result
        return result

    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> List[int]:
    return [number ** power for number in n_tuple]
