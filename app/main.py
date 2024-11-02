from typing import Callable


def cache(func: Callable) -> Callable:
    cache_list = {}

    def storage(*args, **kwargs) -> int:
        if args not in cache_list.keys():
            cache_list[args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_list[args]

    return storage
