from typing import Callable, Any


def cache(func: Callable) -> Callable:
    store = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in store:
            print("Calculating new result")
            result = func(*args, **kwargs)
            store[key] = result
            return result
        else:
            print("Getting from cache")
            return store[key]
    return wrapper
