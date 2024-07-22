from typing import Callable


def cache(func: Callable) -> Callable:

    results_storage = {}

    def inner_checker(*args) -> str:

        if args in results_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results_storage[args] = func(*args)
            
        return results_storage[args]

    return inner_checker
