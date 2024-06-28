from typing import Callable


def cache(func: Callable) -> Callable:

    cache_storage = {}

    def inner(*args) -> int:

        message = "Getting from cache"
        if args not in cache_storage:
            cache_storage[args] = func(*args)
            message = "Calculating new result"

        print(message)
        return cache_storage[args]

    return inner
