from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (func, args)
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]

        result = func(*args)
        cache_storage[key] = result
        print("Calculating new result")
        return result
    return inner
