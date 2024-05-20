from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args: Any) -> Any:
        key = args

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]

        print("Calculating new result")
        result = func(*args)
        cache_storage[key] = result
        return result

    return inner
