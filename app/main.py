from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_of_results = []
    cache_of_args = []

    def wrapper(*args, **kwargs) -> Any:
        nonlocal cache_of_results
        nonlocal cache_of_args

        total_args = args + tuple(kwargs.values())
        if total_args in cache_of_args:
            print("Getting from cache")
            return cache_of_results[cache_of_args.index(total_args)]
        else:
            print("Calculating new result")
            cache_of_results.append(func(*args, **kwargs))
            cache_of_args.append(args + tuple(kwargs.values()))

        return cache_of_results[-1]

    return wrapper
