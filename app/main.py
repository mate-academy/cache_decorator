from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_result = {}

    def innner(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cached_result:
            print("Getting from cache")
            return cached_result[key]
        else:
            results = func(*args, **kwargs)
            cached_result[key] = results
            print("Calculating new result")
            return results

    return innner
