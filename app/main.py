from typing import Callable


def cache(func: Callable) -> Callable:
    stored_dict = {}

    def wrapper(*args: int | tuple, **kwargs: int | tuple) -> int | list[int]:
        if args in stored_dict:
            print("Getting from cache")
            result = stored_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stored_dict[args] = result
        return result
    return wrapper
