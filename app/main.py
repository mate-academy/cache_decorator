from typing import Callable, Any


def cache(func: Callable) -> Callable:
    store = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in store:
            print("Getting from cache")
            return store[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return inner
