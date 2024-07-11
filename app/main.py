from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> int:
        request = func, args + tuple(kwargs.items())
        if request in inner.results:
            print("Getting from cache")
            return inner.results[request]
        else:
            inner.results[request] = func(*args, **kwargs)
            print("Calculating new result")
        return inner.results[request]
    inner.results = {}

    return inner
