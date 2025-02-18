from typing import Callable


def cache(func: Callable) -> Callable:

    completed_runs = {}

    def wrapper(*args) -> dict:

        if tuple(args) in completed_runs:
            print("Getting from cache")
            return completed_runs[tuple(args)]

        print("Calculating new result")
        completed_runs[tuple(args)] = func(*args)
        return completed_runs[tuple(args)]

    return wrapper
