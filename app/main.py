from collections.abc import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        if args not in storage:
            print("Calculating new result")
            return storage.setdefault(args, func(*args))
        else:
            print("Getting from cache")
            return storage.get(args)
    return wrapper
