from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_func = {}
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_func:
            print("Getting from cache")
            return cache_func[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_func[key] = result
            return result
    return wrapper
