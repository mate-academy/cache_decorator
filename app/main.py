from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: tuple[int], **kwargs: dict[int]) -> Any:
        if args in cache_dict:
            print("Getting from cache")

        else:
            print("Calculating new result")
            cache_dict[args] = func(*args, **kwargs)
        return cache_dict[args]
    return wrapper
