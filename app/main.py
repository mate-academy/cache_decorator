from typing import Callable


def cache(func: Callable) -> Callable:
    dict_funcs = {}

    def inner(*args) -> Callable:
        str_func = " ".join(str(val) for val in args)
        if str_func in dict_funcs.keys():
            print("Getting from cache")
        else:
            dict_funcs.update({str_func : func(*args)})
            print("Calculating new result")

        return dict_funcs[str_func]
    return inner
