from typing import Callable
_cache = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args):
        if func not in _cache:
            _cache[func] = {}
        if args not in _cache[func]:
            print("Calculating new result")
            _cache[func][args] = func(*args)
        else:
            print("Getting from cache")

        return _cache[func][args]
    return wrapper
