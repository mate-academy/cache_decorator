from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args):
        completed_runs = []
        result = func(completed_runs)
        for value in (args):
            if value is not isinstance(value, (int, float, str, bool, tuple,)):
                pass
            else:
                completed_runs.append(result)


            if value in ( args):
                return completed_runs
                print("Getting from cache")
            else:
                return func(completed_runs)
                print("Calculating new result")

        return func(args, kwargs)
    return wrapper
