from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cache1 = {}

    def inner(*args, **kwargs) -> Any:
        x = (args + tuple(kwargs))
        if x not in cache1:
            result = func(*args, **kwargs)
            cache1.update({x: result})
            print("Calculating new result")

            return result
        print("Getting from cache")

        return cache1[x]

    return inner
