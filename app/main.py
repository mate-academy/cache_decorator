from typing import Callable, Any


def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args) -> Any:
        if args in func_cache:
            print("Getting from cache")
            return func_cache[args]
        else:
            print("Calculating new result")

            result = func(*args)
            func_cache[args] = result
            return result

    return wrapper
