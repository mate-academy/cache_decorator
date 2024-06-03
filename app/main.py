from typing import Callable


def cache(func: Callable) -> Callable:
    launch_results = {}

    def inner(*args) -> Callable:
        launch_results
        if args in launch_results.keys():
            print("Getting from cache")
        else:
            result = func(*args)
            launch_results[args] = result
            print("Calculating new result")
        return launch_results[args]

    return inner
