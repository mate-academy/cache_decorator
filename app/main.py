from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        arguments = args if args else kwargs
        if arguments not in storage:
            print("Calculating new result")
            func_result = func(*arguments)
            storage[arguments] = func_result
            return func_result
        else:
            print("Getting from cache")
            return storage[arguments]

    return inner
