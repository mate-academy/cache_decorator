from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def checker(*args: Any) -> int:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        cache_dict[args] = func(*args)
        print("Calculating new result")
        return cache_dict[args]

    return checker
