from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            result = func(*args, **kwargs)
            storage[key] = result
            print("Calculating new result")
            return result

    return wrapper

