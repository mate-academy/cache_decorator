from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> int:

        message = "Getting from cache"
        params = (args, frozenset(kwargs))
        if params not in cache_storage:
            cache_storage[params] = func(*args, **kwargs)
            message = "Calculating new result"

        print(message)
        return cache_storage[params]

    return inner
