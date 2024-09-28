from typing import Callable
from functools import wraps
from typing import Any, Tuple


def cache(func: Callable) -> Callable:
    func_cache = {}

    @wraps(func)
    def wrapper(*args: Tuple[Any, ...]) -> Any:
        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            func_cache[args] = result
            return result

    return wrapper
