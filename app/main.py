from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dic = {}

    def wrapper(*args):
        if args in cache_dic:
            print("Getting from cache")
            return cache_dic[args]
        else:
            print("Calculating new result")
            res = func(*args)
            cache_dic[args] = res
            return res
    return wrapper
