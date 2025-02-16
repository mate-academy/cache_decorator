from functools import wraps
from typing import Callable, Any


def is_immutable(obj: Any) -> bool:
    return isinstance(obj, (int, float, str, tuple, bool, type(None)))


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper_cache(*args: Any, **kwargs: Any) -> Any:
        if (
                not all(is_immutable(arg) for arg in args)
                or not all(is_immutable(v) for v in kwargs.values())
        ):
            return func(*args, **kwargs)

        cache_key = (args, tuple(sorted(kwargs.items())) if kwargs else ())

        if cache_key not in wrapper_cache.cache:
            print("Calculating new result")
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = {}
    return wrapper_cache
