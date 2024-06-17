from typing import Callable, Any


def cache(func: Callable) -> Callable:
    test_results = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in test_results:
            print("Getting from cache")
            return test_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            test_results[key] = result
        return result
    return wrapper
