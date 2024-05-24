from typing import Callable


def cache(func: Callable) -> Callable:

    all_cache = {}

    def inner(*args) -> int:
        all_args = []
        for arg in args:
            all_args.append(arg)
        if str(all_args) in all_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            all_cache[str(all_args)] = func(*args)
        return all_cache[str(all_args)]
    return inner
