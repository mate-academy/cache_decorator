from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memo = {}

    def wrapper(*args) -> Any:

        if args in memo:
            print("Getting from cache")
            return memo[args]
        else:
            print("Calculating new result")
            res = func(*args)
            memo[args] = res
            return res

    return wrapper
