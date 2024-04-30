from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage: dict = {}

    def internal(*args) -> Callable:
        current_arguments: tuple = args
        for cached_arguments in cache_storage.keys():
            if current_arguments == cached_arguments:
                print("Getting from cache")
                return cache_storage[cached_arguments]
        print("Calculating new result")
        result = func(*args)
        cache_storage[current_arguments] = result
        return result
    return internal
