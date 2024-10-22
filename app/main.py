from functools import wraps
from typing import Dict, Callable, Any, Tuple


def cache(func: Callable) -> Callable:

    cache_dict: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        # Create cache key from both args and kwargs
        cache_key = (
            tuple(args),  # Convert args to tuple for hashability
            tuple(sorted(kwargs.items()))
        )

        # If result exists in cache, return it
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]

        # If not in cache, calculate new result
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result

    return wrapper
