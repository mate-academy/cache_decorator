from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    def inner(*args: Any) -> Any:
        if args not in cache_results:
            print("Calculating new result")
            result = func(*args)
            cache_results[args] = result
        else:
            print("Getting from cache")
            result = cache_results[args]
        return result
    return inner
