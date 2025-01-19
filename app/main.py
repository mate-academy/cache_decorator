from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args) -> Callable:
        dict_funcs = {}
        str_func = " ".join(str(val) for val in args)
        if str_func in func.__dict__.keys():
            print("Getting from cache")
            return func.__dict__[str_func]
        else:
            print("Calculating new result")
            dict_funcs.update({str_func : func(*args)})
            func.__dict__.update(dict_funcs)
            return dict_funcs[str_func]
    return inner
