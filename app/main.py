from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_results = {}

    def inner(*args: Any) -> Any:
        if args not in cache_results:
            print("Calculating new result")
            cache_results[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_results[args]
    return inner
