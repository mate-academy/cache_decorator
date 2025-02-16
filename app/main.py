from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args):
        completed_runs = {}
        if args in completed_runs:
            print("Getting from cache")
            return completed_runs[args]
        else:
            print("Calculating new result")
            completed_runs[args] = func(*args)
        return completed_runs[args]

    return wrapper
