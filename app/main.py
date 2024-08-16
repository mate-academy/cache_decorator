from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args: Any) -> Any:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        print("Calculating new result")
        result = func(*args)
        stored_results[args] = result
        return result
    return wrapper
