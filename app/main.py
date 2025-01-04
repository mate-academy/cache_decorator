from typing import Callable, Any


cache_dict = {}


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        if f"{func}" in cache_dict:
            if args in cache_dict[f"{func}"]:
                print("Getting from cache")
                return cache_dict[f"{func}"][args]
            else:
                print("Calculating new result")
                cache_dict[f"{func}"][args] = func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
            print("Calculating new result")
            cache_dict[f"{func}"] = {}
            cache_dict[f"{func}"][args] = result
            return result
    return inner
