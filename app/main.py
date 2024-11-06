from typing import Callable, Any


def cache(func: callable) -> Callable:
    cache_result = {}

    def function_cache(*args) -> Any:
        if args not in cache_result:
            cache_result[*args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_result[*args]
    return function_cache
