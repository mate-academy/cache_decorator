from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> Callable:
        results_item = (func, args)
        if results_item in results:
            print("Getting from cache")
            return results[results_item]
        else:
            print("Calculating new result")
            new_result = func(*args)
            results[results_item] = new_result
            return new_result

    return wrapper
