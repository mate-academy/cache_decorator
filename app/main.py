from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_storage:
            print("Calculating new result")
            cache_storage[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_storage.get(args)
    return wrapper
