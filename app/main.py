from typing import Callable


def cache(func: Callable) -> Callable:
    saved_runs = {}

    def wrapper(*args) -> (int, float):
        if args in saved_runs.keys():
            print("Getting from cache")
            return saved_runs[args]
        print("Calculating new result")
        saved_runs[args] = func(*args)
        return saved_runs[args]

    return wrapper
