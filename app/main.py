from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_result = {}

    def innner(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cached_result:
            print("Getting from cache")
            return cached_result[key]

        cached_result[key] = func(*args, **kwargs)
        print("Calculating new result")
        return cached_result[key]

    return innner
