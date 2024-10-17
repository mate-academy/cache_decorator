from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_storage = dict()

    def add_to_storage(func_name: str, args: tuple) -> int:

        func_result = func(*args)
        cache_storage[func_name].add(args)
        cache_storage[func_name + "_res"] = {}
        cache_storage[func_name + "_res"][func_result] = args
        print("Calculating new result")
        return func_result

    @wraps(func)
    def wrapper(*args) -> Callable:

        func_name = func.__name__
        func_result = None

        if func_name in cache_storage:
            if args in cache_storage[func_name]:
                for key, value in cache_storage[func_name + "_res"].items():
                    if value == args:
                        func_result = key
                print("Getting from cache")

            else:
                func_result = add_to_storage(func_name, args)
        else:
            cache_storage[func_name] = set()
            func_result = add_to_storage(func_name, args)

        return func_result

    return wrapper


