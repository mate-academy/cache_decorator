from typing import Callable, Any , Tuple
from functools import wraps

def cache(func: Callable) -> Callable:
    func._cache = {}

    @wraps(func)
    def wrapper(*args: Tuple[Any, ...]) -> Any:
        if args in func._cache:
            print("Getting from cache")
            return func._cache[args]

        print("Calculating new result")
        result = func(*args)
        func._cache[args] = result
        return result

    return wrapper
