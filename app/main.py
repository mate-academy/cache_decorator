from typing import Callable, Any


def cache(func: Callable) -> Callable:
    tuple_data = {}

    def inner(*args, **kwargs) -> Any:
        num = (args,)
        if num in tuple_data:
            print("Getting from cache")
            return tuple_data.get(num)
        else:
            result = func(*args, **kwargs)
            tuple_data[num] = result
            print("Calculating new result")
            return result

    return inner
