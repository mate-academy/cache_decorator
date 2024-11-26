from collections.abc import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage.setdefault(args, func(*args))
        return storage.get(args)

    return wrapper
