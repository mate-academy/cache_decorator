from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> int:
        request = func, args + tuple(kwargs.items())
        if request not in inner.results:
            inner.results[request] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return inner.results[request]
    inner.results = {}

    return inner
