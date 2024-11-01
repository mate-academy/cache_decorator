from typing import Callable


def cache(func: Callable) -> Callable:
    cash = {}

    def decorator(*args, **kwargs) -> int | list:
        el = str(args)
        if el in cash:
            status = "Getting from cache"
        else:
            cash[el] = func(*args, **kwargs)
            status = "Calculating new result"
        print(status)
        return cash[el]

    return decorator
