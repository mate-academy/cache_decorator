from typing import Callable


def cache(func: Callable) -> Callable:
    cashe_result ={}
    def func_results(*args, **kwargs):
        for arg in args:
            if not isinstance(arg,(int,str,float, tuple)):
                print("Value is muttable")
                return
        for keys, value in kwargs.items():
            if not isinstance(value,(int,str,float, tuple)):
                print("Value is muttable")
                return
        names = (args, tuple(kwargs.items()))
        if names in cashe_result:
            print("Getting from cache")
            return cashe_result[names]
        print("Calculating new result")
        res = func(*args, **kwargs)
        cashe_result[names] = res
        return res
    return func_results
