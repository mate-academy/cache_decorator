from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]

        print("Calculating new result")
        results[args] = func(*args)
        return results[args]

    return wrapper
