from typing import Callable


def cache(func: Callable) -> Callable:
    cah = {}

    def warp(*args) -> int:
        if args in cah:
            print("Getting from cache")
            return cah[args]
        else:
            result = func(*args)
            cah[args] = result
            print("Calculating new result")
            return result

    return warp
