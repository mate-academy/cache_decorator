from typing import Callable


def cache(func: Callable) -> Callable:
    save_result = {}

    def inner(*args, **kwargs) -> Callable:
        key_in_save_result = (func.__name__, args,)
        for value in kwargs.values():
            key_in_save_result.add(value)
        if save_result:
            if key_in_save_result in save_result:
                print("Getting from cache")
                return save_result[key_in_save_result]

        print("Calculating new result")
        result = func(*args)
        save_result[key_in_save_result] = result
        return result

    return inner
