from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_cache = {}

    def inner(*args: Any) -> Any:
        if args in results_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results_cache[args] = func(*args)
        return results_cache[args]

    return inner
