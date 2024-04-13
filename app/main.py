from typing import Callable, Any


def cache(func: Callable) -> Callable:
    completed_runs = {}

    def wrapper(*args, **kwargs) -> Any:
        arguments = (args, tuple(kwargs.items()))
        if arguments in completed_runs:
            print("Getting from cache")
            return completed_runs[arguments]
        completed_runs[arguments] = func(*args, **kwargs)
        print("Calculating new result")
        return completed_runs[arguments]

    return wrapper
