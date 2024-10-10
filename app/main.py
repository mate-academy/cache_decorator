from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def inner(*args) -> str:
        if func.__name__ not in cached_results:
            print("Calculating new result")
            cached_results[func.__name__] = {args: func(*args)}
        else:
            if args in cached_results[func.__name__]:
                print("Getting from cache")
            else:
                print("Calculating new result")
                cached_results[func.__name__][args] = func(*args)

        return cached_results[func.__name__][args]

    return inner
