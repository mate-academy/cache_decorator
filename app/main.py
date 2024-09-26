from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            print("Calculating new result")
            wrapper.cache[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return wrapper.cache[cache_key]
    wrapper.cache = {}
    return wrapper
