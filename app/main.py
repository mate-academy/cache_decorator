from typing import Callable, Dict, Tuple


def cache(func: Callable) -> Callable:
    """Caches results of function calls with immutable arguments."""
    cache_store: Dict[Tuple, any] = {}

    def wrapper(*args, **kwargs) -> None:
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in cache_store:
            print("Getting from cache")
            return cache_store[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[cache_key] = result
            return result

    return wrapper


@cache
def long_time_func(aa: int, bb: int, cc: int) -> int:
    return (aa ** bb ** cc) % (aa * cc)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
