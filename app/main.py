from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args):
        if not all(isinstance(arg, (int, float, str, tuple)) for arg in args):
            return func(*args)

        elif args in cached_results:
            print("Getting from cache")
            return cached_results[args]

        print("Calculating new result")
        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper
