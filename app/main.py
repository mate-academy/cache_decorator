from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> None:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache_results:
            print("Getting from cache")
            return cache_results.get(cache_key)
        print("Calculating new result")
        return cache_results.setdefault(cache_key, func(*args, **kwargs))

    return wrapper
