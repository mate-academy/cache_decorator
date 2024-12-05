from typing import Callable


def cache(func: Callable) -> Callable:
    cache = dict()

    def wraper(*args, **kwargs) -> int:
        if args in cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wraper
