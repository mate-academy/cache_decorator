from typing import Callable


def cache(func: Callable) -> Callable:
    caches = {}

    def inner(*args) -> None:
        if args in caches:
            print("Getting from cache")
            return caches[args]
        else:
            print("Calculating new result")
            caches[args] = res = func(*args)
        return res

    return inner


@cache
def long_time_func(num_a: int, num_b: int, num_c: int) -> int:
    return (num_a ** num_b ** num_c) % (num_a * num_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
