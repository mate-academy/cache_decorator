from typing import Callable


def cache(func: Callable) -> Callable:
    saved_runs = {}

    def wrapper(*args) -> (int, float):
        if args not in saved_runs.keys():
            print("Calculating new result")
            saved_runs[args] = func(*args)
            return saved_runs[args]
        else:
            print("Getting from cache")
            return saved_runs[args]
    return wrapper
