from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    def inner(*args: list) -> Callable:
        key = hash(args)

        if key in store:
            print("Getting from cache")

            return store[key]

        print("Calculating new result")

        res = func(*args)
        store[key] = res

        return res

    return inner

