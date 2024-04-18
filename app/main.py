from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache1 = {}

    def inner(*args, **kwargs) -> Any:
        func_input = (args + tuple(kwargs))
        if func_input not in cache1:
            result = func(*args, **kwargs)
            cache1.update({func_input: result})
            print("Calculating new result")

            return result
        print("Getting from cache")

        return cache1[func_input]

    return inner
