from typing import Callable


def cache(func: Callable) -> Callable:

    completed_runs = {}

    def check_if_repeated(*args) -> Callable:
        args_str = "".join([str(arg) for arg in args])
        cached_value = completed_runs.get(args_str)
        if cached_value is not None:
            print("Getting from cache")
            return cached_value
        else:
            print("Calculating new result")
            value_to_cache = func(*args)
            completed_runs[args_str] = value_to_cache
            return value_to_cache
    return check_if_repeated
