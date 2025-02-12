from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def cache_wrapper(*args: tuple) -> any:
        if (cached := cache_memory.get(args)) is not None:
            print("Getting from cache")
            return cached

        print("Calculating new result")
        cache_memory[args] = func(*args)

        return cache_memory[args]

    return cache_wrapper
