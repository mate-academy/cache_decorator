from typing import Callable


def cache(func: Callable) -> Callable:
    saved_runs = {}

    def arg_saver(*args, **kwargs) -> callable:
        arg = str(args) + str(kwargs)
        if arg in saved_runs:
            print("Getting from cache")
            return saved_runs[arg]
        else:
            result = func(*args, **kwargs)
            saved_runs.update({arg: result})
            print("Calculating new result")
            return result
    return arg_saver
