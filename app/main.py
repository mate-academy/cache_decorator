from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    # Store cache per function
    func_cache: dict[tuple, any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        # Use the arguments as the cache key
        cache_key = (func.__name__, args, tuple(sorted(kwargs.items())))

        # Use a ternary operator to either return
        # the cached value or calculate a new result
        result = func_cache[cache_key] \
            if cache_key in func_cache else func(*args, **kwargs)

        # Print messages based on whether
        # the result was cached or newly calculated
        print("Getting from cache"
              if cache_key in func_cache else "Calculating new result")

        # Store the result in the cache if it was newly calculated
        if cache_key not in func_cache:
            func_cache[cache_key] = result

        return result

    return wrapper
