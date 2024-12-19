from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any) -> Any:
        storage_keys = storage.keys()
        if args not in storage_keys:
            print("Calculating new result")
            result = func(*args)
            storage[args] = result
        else:
            print("Getting from cache")
            result = storage[args]
        return result
    return wrapper
