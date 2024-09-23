from typing import Any, Callable

from functools import wraps


def cache(func: Callable) -> Callable:

    data = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        data_type = [args]
        if func in data and args in data[func]:
            print("Getting from cache")
            return data[func][data[func].index(args) + 1]

        elif func not in data:
            data.update({func: data_type})

        elif args not in data[func]:
            data[func].append(args)

        result = func(*args, **kwargs)
        data[func].append(result)
        print("Calculating new result")
        return result

    return inner
