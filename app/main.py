from functools import wraps
from typing import Callable, Dict, Any, Hashable


def is_immutable(value: Any) -> bool:
    """Check if a value is immutable."""
    return isinstance(value, (int, float, str, tuple, frozenset, bool, type(None)))


def make_cache_key(args: tuple, kwargs: dict) -> Hashable:
    """Create a cache key that is a combination of args and frozenset for kwargs."""
    return (args, frozenset(kwargs.items()))


def cache(func: Callable) -> Callable:
    # Storage for cached results
    cache_storage: Dict[Hashable, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check for immutability in all positional arguments
        for arg in args:
            if not is_immutable(arg):
                raise TypeError(f"Mutable argument {arg} of type {type(arg)} is not allowed for caching.")

        # Check for immutability in all keyword arguments
        for key, value in kwargs.items():
            if not is_immutable(value):
                raise TypeError(f"Mutable argument {key}={value} of type {type(value)} is not allowed for caching.")

        # Create a cache key from positional arguments and frozenset of keyword arguments
        cache_key = make_cache_key(args, kwargs)

        # If the cache key exists, return the cached result
        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            # Calculate the result and store it in cache
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[cache_key] = result
            return result

    return wrapper



