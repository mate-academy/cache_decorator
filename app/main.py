from typing import Callable
_CACHE = {}


def cache(func: Callable) -> Callable:
    def wrapper(*args: int) -> int:
        if func not in _CACHE:
            _CACHE[func] = {}
        if args not in _CACHE[func]:
            _CACHE[func][args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return _CACHE[func][args]
    return wrapper
