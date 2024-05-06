from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))
        if key in store:
            print("Getting from cache")
            return store.get(key)

        value = func(*args, **kwargs)
        store[key] = value
        print("Calculating new result")
        return value

    return wrapper
