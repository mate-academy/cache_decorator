from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    # Dictionary to store cache for each function
    cache_dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a cache key from arguments
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[cache_key] = result
            return result

    return wrapper
