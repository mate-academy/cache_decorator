from typing import Callable


def cache(func: Callable) -> Callable:
    result_dic = {}

    def wrapper(*args) -> Callable:
        if args not in result_dic:
            print("Calculating new result")
            result = func(*args)
            result_dic[args] = result
            return result
        else:
            print("Getting from cache")
            return result_dic[args]
    return wrapper
