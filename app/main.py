from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data: dict = {}

    def wrapper(*args, **kwargs) -> int:
        key = ",".join(str(arg) for arg in args)

        if key in cache_data:
            print("Getting from cache")
        else:
            cache_data[key] = func(*args, **kwargs)
            print("Calculating new result")

        return cache_data[key]

    return wrapper
