from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(a, b, *args) -> str:
        key = (a, b, *args)
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        cache_dict[key] = func(a, b, *args)
        print("Calculating new result")
        return cache_dict[key]

    return inner
