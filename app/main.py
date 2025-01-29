from typing import Callable


def cache(func: Callable) -> Callable:
    cache_result = {}


    def func_results(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, str, float, tuple)):
                print("Value is mutable")
                return
        for keys, value in kwargs.items():
            if not isinstance(value, (int, str, float, tuple)):
                print("Value is mutable")
                return
        names = (args, tuple(kwargs.items()))
        if names in cache_result:
            print("Getting from cache")
            return cache_result[names]
        print("Calculating new result")
        res = func(*args, **kwargs)
        cache_result[names] = res
        return res
    return func_results
