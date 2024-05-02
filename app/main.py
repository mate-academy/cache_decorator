from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage: dict = {}

    def internal(*args, **kwargs) -> Callable:
        current_arguments: tuple = (args, tuple(kwargs.items()))
        if current_arguments in cache_storage:
            print("Getting from cache")
            return cache_storage[current_arguments]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[current_arguments] = result
        return result
    return internal
