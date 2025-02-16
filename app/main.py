from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storange = {}

    def inner(*args, **kwargs):
        if func not in cache_storange:
            cache_storange[func] = {}

        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storange[func]:
            print("Getting from cache")
            return cache_storange[func][key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storange[func][key] = result
            return result

    return inner