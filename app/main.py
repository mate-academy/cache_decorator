from functools import wraps
from typing import Callable, Dict, Any


def is_immutable(value: Any) -> bool:
    """Check if a value is immutable."""
    return isinstance(value, (int, float, str, tuple, frozenset, bool, type(None)))


def cache(func: Callable) -> Callable:
    cache_storage: Dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not is_immutable(arg):
                raise TypeError(f"Mutable argument {arg} of type {type(arg)} is not allowed for caching.")

        for key, value in kwargs.items():
            if not is_immutable(value):
                raise TypeError(f"Mutable argument {key}={value} of type {type(value)} is not allowed for caching.")

        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[cache_key] = result
            return result

    return wrapper





