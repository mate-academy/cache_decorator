from typing import Callable, Any


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        return result
    return wrapper

