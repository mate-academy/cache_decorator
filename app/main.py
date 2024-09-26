from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def inner(*args) -> int:
        if args in cache_memory:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_memory[args] = func(*args)
        return cache_memory[args]
    return inner
