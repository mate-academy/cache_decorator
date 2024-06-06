from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage_cache = {}

    @wraps(func)
    def warp(*args, **kwargs) -> Callable:
        hash_key = (args, frozenset(kwargs.items()))
        if hash_key in storage_cache:
            print("Getting from cache")
            return storage_cache[hash_key]
        else:
            result = func(*args, **kwargs)
            storage_cache[hash_key] = result
            print("Calculating new result")
            return result

    return warp
