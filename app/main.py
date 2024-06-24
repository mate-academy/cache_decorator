from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def results_func(*args: tuple[Any]) -> Any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        print("Calculating new result")
        result = func(*args)
        cache_dict[args] = result
        return result

    return results_func
