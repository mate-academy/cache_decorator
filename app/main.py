from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict.get(args)

        print("Calculating new result")
        func_result = func(*args)
        cache_dict[args] = func_result

        return func_result

    return wrapper
