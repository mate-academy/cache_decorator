from typing import Any, Callable

data = []


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        aray = []
        aray.append(func)
        aray.append(args)
        if aray not in data:
            data.append(aray)
            result = func(*args)
            data.append(result)
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return data[data.index(aray) + 1]

    return inner
