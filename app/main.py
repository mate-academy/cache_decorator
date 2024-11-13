from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        result = func(*args, **kwargs)
        return result
    return wrapper

