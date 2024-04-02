from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (*args, *kwargs.items())

        if key in dict_cache:
            print("Getting from cache")
            return dict_cache[key]

        result = func(*args, **kwargs)
        dict_cache[key] = result
        print("Calculating new result")
        return result

    return wrapper
