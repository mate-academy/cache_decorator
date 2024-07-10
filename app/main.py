from typing import Callable

saved_runs = {}


def cache(func: Callable) -> Callable:
    def arg_saver(*argv, **argc) -> callable:
        arg = str(argv) + str(argc) + str(func)
        if arg in saved_runs:
            print("Getting from cache")
            return saved_runs[arg]
        else:
            result = func(*argv, **argc)
            saved_runs.update({arg: result})
            print("Calculating new result")
            return result
    return arg_saver
