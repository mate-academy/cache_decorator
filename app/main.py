from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_storage:
            print("Calculating new result")
            function_result = func(*args, **kwargs)
            cache_storage[args] = function_result
            return function_result
        else:
            print("Getting from cache")
            return cache_storage.get(args)

    wrapper.cache_storage = cache_storage
    return wrapper
