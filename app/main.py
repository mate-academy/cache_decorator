from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def process_cache(*args: Any) -> Any:
        if args not in cached_results:
            print("Calculating new result")
            cached_results[args] = func(*args)
        else:
            print("Getting from cache")
        return cached_results[args]

    return process_cache
