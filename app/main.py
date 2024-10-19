from typing import Callable


def cache(func: Callable) -> Callable:
    """Caching decorator."""
    cache_store = {}  # Dictionary to store cached results

    def wrapper(*args) -> Callable:
        # Check if the result for given arguments is already cached
        if (func, args) in cache_store:
            print("Getting from cache")
            return cache_store[(func, args)]
        else:
            # If not cached, calculate the result and store it in the cache
            print("Calculating new result")
            result = func(*args)
            cache_store[(func, args)] = result
            return result

    return wrapper
