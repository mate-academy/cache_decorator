from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def inner(*args) -> int:
        key = args
        if key in cache_memory:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_memory[key] = func(*args)
        return cache_memory[key]
    return inner
