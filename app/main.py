from typing import Callable
from typing import Union


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def check_cache(*args) -> Union[int, list]:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        print("Calculating new result")
        cache_dict[args] = func(*args)
        return cache_dict[args]

    return check_cache


@cache
def long_time_func(first_value: int, second_value: int, third_value: int) -> int:
    return (first_value ** second_value ** third_value) % (first_value * third_value)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
