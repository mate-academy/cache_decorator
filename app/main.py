from typing import Callable, Any, Tuple


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> tuple[Any, ...] | Any:
        results_item = tuple(args)
        if results_item in results:
            return results[results_item]
        else:
            new_result = tuple(args)
            results[results_item] = new_result
            return new_result

    return wrapper
