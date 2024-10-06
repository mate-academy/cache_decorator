from typing import Callable


def cache(func: Callable) -> Callable:
    save_result = {}

    def inner(*args) -> Callable:
        if save_result:
            key_in_save_result = (func, args,)
            if key_in_save_result in save_result:
                print("Getting from cache")
                return save_result[key_in_save_result]
            else:
                print("Calculating new result")
                result = func(*args)
                save_result[(func, args,)] = result
                return result
        else:
            print("Calculating new result")
            result = func(*args)
            save_result[(func, args,)] = result
            return result

    return inner
