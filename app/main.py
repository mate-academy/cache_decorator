from typing import Callable


def cache(func: Callable) -> Callable:
    cache_box = {}   # Create dict

    def wrapper(*args, **kwargs) -> None:
        if args not in cache_box:
            result = func(*args, **kwargs)

            cache_box[args] = result          # Adding data that doesn't exist
            print("Calculating new result")
        else:
            result = cache_box[args]      # We take it from the kush
            print("Getting from cache")
        return result
    return wrapper

