from typing import Any, Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args: Any) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result

    return wrapper
