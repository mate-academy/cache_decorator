from typing import Any, Callable

from functools import wraps


def cache(func: Callable) -> Callable:

    data = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        data_type = [args, kwargs]
        if func in data and (data_type in data[func]):
            print("Getting from cache")
            return data[func][data[func].index(data_type) + 1]

        elif func not in data:
            data.update({func: [data_type]})

        elif data_type not in data[func]:
            data[func].append(data_type)

        result = func(*args, **kwargs)
        data[func].append(result)
        print("Calculating new result")
        return result

    return inner
