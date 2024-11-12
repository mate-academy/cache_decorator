from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        data_iterable = (args, frozenset(kwargs.items()))
        if data_iterable not in cache_dict:
            print("Calculating new result")
            cache_dict[data_iterable] = func(*args, **kwargs)
            return cache_dict[data_iterable]
        print("Getting from cache")
        return cache_dict[data_iterable]

    return wrapper
