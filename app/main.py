from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        print("Getting from cache" if key in cached_results
              else "Calculating new result")

        return cached_results[key] if key in cached_results \
            else cached_results.setdefault(key, func(*args, **kwargs))

    return wrapper
