from typing import Callable, Dict, Tuple


def cache(func: Callable) -> Callable:
    cache_store: Dict[Tuple, any] = {}


    def wrapper(*args):
        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result
    return wrapper()
