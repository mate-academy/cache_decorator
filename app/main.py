from typing import Callable, Any

def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in storage:
            print("Getting from cache")
            result = storage[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[args] = result
        return result
    return wrapper
