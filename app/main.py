from typing import Callable


def make_hashable(obj: (list, dict, set)) -> (tuple, frozenset):
    """Преобразует объект в хэшируемую структуру."""
    if isinstance(obj, list):
        return tuple(obj)
    elif isinstance(obj, dict):
        return tuple(sorted(obj.items()))
    elif isinstance(obj, set):
        return frozenset(obj)
    else:
        return obj


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        key = tuple(make_hashable(arg) for arg in args)

        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[key] = result
            return result

    return wrapper
