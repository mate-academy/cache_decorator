from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Callable:
        dict_key = (*args, tuple(kwargs.items()))

        if dict_key in cache_dict:
            print("Getting from cache")
            return cache_dict[dict_key]
        else:
            function_result = func(*args, **kwargs)
            cache_dict[dict_key] = function_result

            print("Calculating new result")
            return function_result

    return inner
