from typing import Callable


def cache(func: Callable) -> Callable:

    allredy = {}

    def wraper(*args, **kvargs) -> int:
        nonlocal allredy
        if args in [k for k in allredy]:
            print("Getting from cache")
            return allredy[args]
        else:
            print("Calculating new result")
            res = func(*args, **kvargs)
            allredy[args] = res
            return res
    return wraper
