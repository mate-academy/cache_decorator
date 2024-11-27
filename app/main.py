from typing import Callable, Any


def cache(func: Callable) -> Any:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = tuple(args, *kwargs.items())
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            result = func(*args, **kwargs)
            results[key] = result
            print("Calculating new result")
            return result
    return wrapper
