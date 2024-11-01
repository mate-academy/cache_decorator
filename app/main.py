from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage_cache = {}

    def wrapper(*args) -> Any:

        key = args

        if key in storage_cache:
            print("Getting from cache")
            return storage_cache[key]

        print("Calculating new result")
        result = func(*args)
        storage_cache[key] = result
        return result

    return wrapper
