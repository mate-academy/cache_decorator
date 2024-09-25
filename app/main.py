from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def inner(*args) -> int:
        key = tuple([*args])
        if key in cache_memory:
            print("Getting from cache")
            return cache_memory[key]
        cache_memory[key] = func(*args)
        print("Calculating new result")
        return cache_memory[key]
    return inner
