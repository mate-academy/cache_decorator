from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args, **kwargs):
        if func not in cache_storage:
            cache_storage[func] = {}

        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage[func]:
            print("Getting from cache")
            return cache_storage[func][key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[func][key] = result
            return result

    return inner