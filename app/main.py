from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}
    def wrapper(*args, **kwargs) -> Any:
        key_result = (args, tuple(kwargs.items()), func.__name__)
        if key_result in result.keys():
            print("Getting from cache")
        else:
            result[key_result] = func(*args, **kwargs)
            print("Calculating new result")
        return result[key_result]
    return wrapper
