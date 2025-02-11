from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> int:

        key = (args, frozenset(kwargs.items())) if kwargs else args

        print("Getting from cache" if key in storage
              else "Calculating new result")
        return storage[key] if key in storage \
            else storage.setdefault(key, func(*args, **kwargs))

    return wrapper
