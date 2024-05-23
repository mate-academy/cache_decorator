from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    saved_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        frozen_kwargs = frozenset(kwargs.items())
        if (args, frozen_kwargs) in saved_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            saved_results[(args, frozen_kwargs)] = func(*args, **kwargs)
        return saved_results[(args, frozen_kwargs)]

    return wrapper
