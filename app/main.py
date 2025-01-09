from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    results_function_execution = {}

    @wraps(func)
    def wrapper(*args) -> int:
        execution_result = results_function_execution.get(args)
        if execution_result is not None:
            print("Getting from cache")
            return execution_result
        else:
            print("Calculating new result")
            execution_result = func(*args)
            results_function_execution[args] = execution_result
            return execution_result
    return wrapper
