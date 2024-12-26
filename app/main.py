from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> Any:
        if args in results:
            print("Getting from cache")
            return results[args]
        results.update({args: func(*args)})
        print("Calculating new result")
        return results[args]
    return wrapper
