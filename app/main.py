from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:

    results = {}

    def inner(*args) -> Any:

        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results[args] = func(*args)
        return results[args]

    return inner
