from typing import Callable, Any


def cache(func: Callable) -> Any:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            result = func(*args)
            results[args] = result
            print("Calculating new result")
            return result
    return wrapper
