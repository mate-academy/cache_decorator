from typing import Callable, Any


def cache(func: Callable) -> Any:
    save_data = {}

    def inner(*args) -> Any:
        if args in save_data:
            print("Getting from cache")
            return save_data[args]
        else:
            print("Calculating new result")
            result = func(*args)
            save_data[args] = result
        return result
    return inner
