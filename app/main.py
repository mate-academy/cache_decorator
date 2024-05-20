from typing import Callable


def cache(func: Callable) -> Callable:
    my_cache = {}

    def wrapper(*args: list, **kwargs: dict) -> None:
        dict_key = (*args, tuple(kwargs.items()))

        if (*args, tuple(kwargs.items())) in my_cache:
            print("Getting from cache")
        else:
            my_cache[dict_key] = func(*args, **kwargs)
            print("Calculating new result")
        return my_cache[dict_key]

    return wrapper
