from typing import Callable


def cache(func: Callable) -> Callable:

    all_cache = {}

    def wrapper(*args, **kwargs) -> int:
        if args in all_cache:
            print("Getting from cache")
            return all_cache[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            all_cache[args] = result
            return result

    return wrapper
