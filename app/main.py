from typing import Any, Callable
from functools import wraps

def cache(func: Callable) -> Callable:
    data = []
    @wraps(func)
    def inner(*args) -> Any:
        data_type = [func, args]
        if data_type not in data:
            data.append(data_type)
            result = func(*args)
            data.append(result)
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return data[data.index(data_type) + 1]

    return inner
