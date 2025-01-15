from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_data = {}

    def inner(*args, **kwargs) -> Any:
        key = (args,)
        if key in stored_data:
            print("Getting from cache")
            return stored_data.get(key)
        else:
            result = func(*args, **kwargs)
            stored_data[key] = result
            print("Calculating new result")
            return result
    return inner
