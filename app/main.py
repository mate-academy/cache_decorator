from typing import Callable, Any, Dict, Tuple, Hashable


def cache(func: Callable) -> Callable:
    cache_store: Dict[Callable, Dict[Tuple[Hashable, ...], Any]] = {}

    def wrapper(*args, **kwargs) -> Any:
        if func not in cache_store:
            cache_store[func] = {}
        key = (args, frozenset(kwargs.items()))

        if key in cache_store[func]:
            print("Getting from cache")
            return cache_store[func][key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_store[func][key] = result
        return result

    return wrapper
