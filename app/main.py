from typing import Callable


def cache(func: Callable) -> Callable:
    func.cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in func.cache:
            print("Getting from cache")
            return func.cache[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        func.cache[key] = result
        return result

    return wrapper