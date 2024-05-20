from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> int | list[int]:
        if args in stored_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_dict[args] = func(*args, **kwargs)
        return stored_dict[args]
    return wrapper
