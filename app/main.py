from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_result:
            print("Getting from cache")
            return cache_result[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_result[key] = result
        return result

    return wrapper
