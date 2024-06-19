from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs) -> Any:
        info = (args, func.__name__)
        if info in cache_store:
            print("Getting from cache")
            return cache_store[info]

        print("Calculating new result")
        new_result = func(*args, **kwargs)
        cache_store[info] = new_result
        return new_result

    return wrapper
