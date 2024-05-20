from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_ = {}

    def inner(*args: Any) -> Any:
        if args in cache_:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_[args] = func(*args)
        return cache_[args]
    return inner
