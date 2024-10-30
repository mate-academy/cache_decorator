from typing import Callable

def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> int:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[args] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, mod: int) -> int:
    return (base ** exponent) % mod


@cache
def long_time_func_2(numbers: tuple, power: int) -> list:
    return [number ** power for number in numbers]

