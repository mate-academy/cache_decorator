from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def inner(*args: tuple) -> Any:
        if args in results_cache:
            print("Getting from cache")
            return results_cache[args]

        else:
            print("Calculating new result")
            result = func(*args)
            results_cache[args] = result
            return result

    return inner
