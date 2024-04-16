from typing import Callable


def cache(func: Callable) -> Callable:
    store_result = {}

    def inner(*args) -> tuple:
        tuple_param = args
        if tuple_param in store_result.keys():
            print("Getting from cache")
            return store_result[tuple_param]
        print("Calculating new result")
        store_result[tuple_param] = func(*args)
        return store_result[tuple_param]

    return inner
