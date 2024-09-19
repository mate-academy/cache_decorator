from typing import Any, Callable


def cache(func: Callable) -> Callable:
    caches = {}

    def wrapper(*args) -> Any:
        if func not in caches:
            caches[func] = {}
        if args in caches[func]:
            print("Getting from cache")
            return caches[func][args]
        else:
            print("Calculating new result")
            fin = func(*args)
            caches[func][args] = fin
            return fin

    return wrapper
