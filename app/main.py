from typing import Callable, Dict, Tuple, Any


def cache(func: Callable) -> Callable:
    """
    A decorator that caches the results of function
    calls with immutable arguments.

    Note: This decorator should only be used with functions
    that take immutable arguments (e.g., int, str, tuple).
    """
    cache_store: Dict[Tuple, Any] = {}

    def wrapper(*args) -> Any:
        # Ensure all arguments are immutable
        if not all(isinstance(arg, (int, float, str, tuple)) for arg in args):
            raise ValueError(
                "All arguments must be immutable (int, float, str, tuple)."
            )

        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result

    return wrapper
