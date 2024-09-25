from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_dict_key = (args, tuple(sorted(kwargs.items())))
        if cache_dict_key in cache_dict:
            print("Getting from cache")
            result = cache_dict[cache_dict_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_dict_key] = result

        return result

    return wrapper
