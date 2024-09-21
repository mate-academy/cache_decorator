from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Callable:

        if args in cache_storage:
            print("Getting from cache")
            result = cache_storage[args]["result"]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = {"args": args, "result": result}

        return result

    return wrapper
