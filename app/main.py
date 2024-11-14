from typing import Callable, Any


def cache(func: Callable) -> Any:
    results = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in results:
            print(f"Getting from cache {results[args]}")
        else:
            result = func(*args)
            results[args] = result
            print(f"Calculating new result {result}")
    return wrapper
