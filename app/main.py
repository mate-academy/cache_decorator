from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dictionary = {}

    def inner(*args, **kwargs) -> Any:
        cache_item = func.__name__ + "".join(str(args)) + "".join(str(kwargs))
        if cache_item in cache_dictionary:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dictionary[cache_item] = func(*args, **kwargs)
        return cache_dictionary[cache_item]
    return inner
