from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        print("Calculating new result")
        cached_results[key] = func(*args, **kwargs)
        return cached_results[key]

    return wrapper
