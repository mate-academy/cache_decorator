from typing import Callable, Dict, Any


def cache(func: Callable) -> Callable:
    results_cache: Dict[tuple, Any] = {}

    def inner(*args, **kwargs) -> Callable:
        try:
            if args in results_cache:
                print("Getting from cache")
                return results_cache[args]
            else:
                print("Calculating new result")
                result = func(*args, **kwargs)
                results_cache[args] = result
                return result
        except TypeError:
            print("Arguments are not hashable, calculating without caching")
            return func(*args, **kwargs)

    return inner
