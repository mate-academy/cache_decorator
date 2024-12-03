from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args) -> None:
        if func.__name__ in results and args in results[func.__name__]:
            print("Getting from cache")
            return results[func.__name__][args]

        print("Calculating new result")
        result = func(*args)
        if func.__name__ not in results:
            results[func.__name__] = {}

        results[func.__name__][args] = result

        return result

    return inner
