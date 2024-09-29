from typing import Callable, Dict, Tuple, Any
import functools


def cache(func: Callable) -> Callable:
    cache_storage: Dict[str, Dict[Tuple, Any]] = {}

    @functools.wraps(func)
    def wrapper(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = (func.__name__, args, kwargs_tuple)

        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        cache_storage[cache_key] = result
        return result

    return wrapper
