from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict: dict = {}

    def wrapper(*args) -> int:

        template = ",".join(str(arg) for arg in args)
        if template in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[template] = func(*args)
            print("Calculating new result")

        return cache_dict[template]

    return wrapper
