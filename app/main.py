from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:

    function_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        function_cache_key = (args, tuple(kwargs.items()))
        if function_cache_key in function_cache:
            print("Getting from cache")
            return function_cache[function_cache_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        function_cache[function_cache_key] = result
        return result
    return wrapper
