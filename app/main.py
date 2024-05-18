from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory = dict()

    def wrapper(*args, **kwargs) -> Any:
        key = (*args, *kwargs.items())
        if key in memory:
            print("Getting from cache")
            result = memory[key]
        else:
            memory_new = func(*args, **kwargs)
            memory[key] = memory_new
            print("Calculating new result")
            result = memory_new
        return result

    return wrapper
