from typing import Callable


def make_hashable(args):
    hashable_args = []
    for arg in args:
        if isinstance(arg, (list, set)):
            hashable_args.append(tuple(arg))
        elif isinstance(arg, dict):
            hashable_args.append(tuple(sorted(arg.items())))
        else:
            hashable_args.append(arg)
    return tuple(hashable_args)


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args) -> Callable:
        hashable_args = make_hashable(args)
        if hashable_args in cache_store:
            print("Getting from cache")
            return cache_store[hashable_args]
        print("Calculating new result")
        result = func(*args)
        cache_store[hashable_args] = result
        return result
    return inner
