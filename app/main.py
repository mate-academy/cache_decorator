from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_of_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        keys = (args, *kwargs.items())

        if func not in cache_of_results:
            cache_of_results[func] = {}

        if keys in cache_of_results[func]:
            print("Getting from cache")
            return cache_of_results[func][keys]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_of_results[func][keys] = result
        return result
    return wrapper
