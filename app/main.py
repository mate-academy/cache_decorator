from typing import Callable


def cache(func: Callable, **dict_funcs) -> Callable:
    def inner(*args, **dict_of_element) -> Callable:
        str_func = " ".join(str(val) for val in args)
        if str_func in dict_funcs.keys():
            print("Getting from cache")
            return dict_funcs[str_func]
        else:
            dict_of_element = {str_func : func(*args)}
            dict_funcs.update(dict_of_element)
            print("Calculating new result")
            return dict_of_element[str_func]
    return inner
