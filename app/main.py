from typing import Callable


def cache(func: Callable) -> Callable:
    save_result = {}

    def inner(*args, **kwargs) -> Callable:
        key_in_save_result = (func.__name__, args, tuple(kwargs.items()))
        if save_result:
            if key_in_save_result in save_result:
                print("Getting from cache")
                return save_result[key_in_save_result]

        print("Calculating new result")
        result = func(*args, **kwargs)
        save_result[key_in_save_result] = result
        return result

    return inner
