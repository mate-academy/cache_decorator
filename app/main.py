from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_data = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in cash_data:
            print("Getting from cache")
            return cash_data.get(args)
        print("Calculating new result")
        result = func(*args, **kwargs)
        cash_data[args] = result
        return result

    return wrapper
