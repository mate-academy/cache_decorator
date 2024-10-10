from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> tuple[Any, ...] | Any:
        cache_key = tuple(args)
        if cache_key in results:
            print("Getting from cache")
            return results[cache_key]
        else:
            print("Calculating new result")
            new_result = func(*args)
            results[cache_key] = new_result
            return new_result

    return wrapper
