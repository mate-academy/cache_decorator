from typing import Callable


def cache(func: Callable) -> Callable:

    completed_runs = {}

    def wrapper(*args) -> dict:

        argumenty = (tuple(args))

        if argumenty in completed_runs:
            print("Getting from cache")
            return completed_runs[argumenty]
        else:
            print("Calculating new result")
            completed_runs[argumenty] = func(*args)

        return completed_runs[argumenty]

    return wrapper
