from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}
    
    def inner(*args):
        if args in cache:
           return cache[args]
        else:
           result = func(*args)
           cache[args] = result
        return result
    
    return inner
