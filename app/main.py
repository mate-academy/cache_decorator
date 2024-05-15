from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def generate_key(*arg, **kwargs) -> str:
        func_name = func.__name__
        arg_name = str(arg)
        kwargs_name = str(kwargs)
        return f"{func_name} {arg_name} {kwargs_name}"

    def wrapper(*arg, **kwargs) -> Callable:
        key = generate_key(*arg, **kwargs)

        if results.get(key) is not None:
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        result = func(*arg, **kwargs)
        results[key] = result
        return result
    return wrapper
