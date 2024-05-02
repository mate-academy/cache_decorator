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
def long_time_func(value_1st: int, value_2nd: int, value_3rd: int) -> int:
    return (value_1st ** value_2nd ** value_3rd) % (value_1st * value_3rd)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
