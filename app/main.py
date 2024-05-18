from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage.get(args)
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[args] = result
        return storage.get(args)
    return wrapper
