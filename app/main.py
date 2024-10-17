from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_storage = dict()

    def add_to_storage(func_name: str, args: tuple) -> int:

        func_result = func(*args)
        launch_in = str(args)
        cache_storage[func_name][launch_in] = func_result
        print("Calculating new result")
        return func_result

    @wraps(func)
    def wrapper(*args) -> Callable:

        func_name = func.__name__
        func_result = None

        if func_name in cache_storage:
            if str(args) in cache_storage[func_name]:
                func_result = cache_storage[func_name][str(args)]
                print("Getting from cache")
            else:
                func_result = add_to_storage(func_name, args)
        else:
            cache_storage[func_name] = dict()
            func_result = add_to_storage(func_name, args)

        return func_result

    return wrapper
