from typing import Callable, Any
from functools import wraps

function_caches = {}


def cache(func: Callable) -> Callable:
    function_caches[func] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in function_caches[func]:
            print("Getting from cache")
            return function_caches[func][key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        function_caches[func][key] = result
        return result

    return wrapper