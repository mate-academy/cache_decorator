from typing import Callable, Any


def cache(func: Callable) -> Callable:

    data_cache = {}

    def result_cache(*args, **kwargs) -> Any:
        if args in data_cache:
            print("Getting from cache")
            return data_cache.get(args)
        print("Calculating new result")
        result = func(*args, **kwargs)
        data_cache[args] = result
        return result

    return result_cache
