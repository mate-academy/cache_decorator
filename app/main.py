from typing import Callable, Any


def cache(func: Callable) -> Callable:
    caches = {}

    def wraper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in caches:
            print("Getting from cache")
            return caches[key]
        else:

            print("Calculating new result")
            result = func(*args, **kwargs)
            caches[key] = result
            return result
    return wraper
