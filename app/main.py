from typing import Callable, Any


def cache(func: Callable) -> Callable:
    results_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in results_storage:
            print("Getting from cache")
            return results_storage.get(args)
        print("Calculating new result")
        result = func(*args, **kwargs)
        results_storage[args] = result
        return results_storage.get(args)
    return wrapper
