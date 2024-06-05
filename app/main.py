from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_of_results = {}

    def wrapper(*args, **kwargs) -> Any:
        nonlocal cache_of_results

        keys = args + tuple(kwargs.items())

        if keys in cache_of_results:
            print("Getting from cache")

        else:
            print("Calculating new result")
            cache_of_results[keys] = func(*args, **kwargs)

        return cache_of_results[keys]

    return wrapper
