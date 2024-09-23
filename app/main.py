from typing import Callable, Dict, Any


def cache(func: Callable) -> Callable:
    results_cache: Dict[tuple, Any] = {}

    def inner(*args, **kwargs) -> Callable:
        if kwargs:
            kwargs_tuple = tuple(sorted(kwargs.items()))
        else:
            kwargs_tuple = ()

        cache_key = args + kwargs_tuple
        try:
            if args in results_cache:
                print("Getting from cache")
                return results_cache[cache_key]
            else:
                print("Calculating new result")
                result = func(*args, **kwargs)
                results_cache[cache_key] = result
                return result
        except TypeError:
            print("Arguments are not hashable, calculating without caching")
            return func(*args, **kwargs)

    return inner
