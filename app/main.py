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
