from typing import Callable, Any


def cache(func: Callable) -> Callable:
    completed_runs = {}

    def wrapper(*args) -> Any:
        if args in completed_runs:
            print("Getting from cache")
            return completed_runs[args]
        completed_runs[args] = func(*args)
        print("Calculating new result")
        return completed_runs[args]

    return wrapper
