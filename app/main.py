from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage: dict = {}

    def internal(*args, **kwargs) -> Callable:
        argument_list: list = [args, kwargs]
        for cached_result, cached_arguments in cache_storage.items():
            if argument_list == cached_arguments:
                print("Getting from cache")
                return cached_result
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[result] = argument_list
        return result
    return internal
