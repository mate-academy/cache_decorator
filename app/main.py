from typing import Callable


def cache(func: Callable) -> Callable:
    global_memmory = {}
    def wrapped(*args, **kwargs) -> any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in global_memmory:
            print("Getting from cache")
            return global_memmory[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            global_memmory[key] = result
            return result


    return wrapped

