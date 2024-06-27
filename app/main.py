from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """
    decorating only functions that take immutable arguments.
    cache should print "Getting from cache" when returns stored value
    and "Calculating new result" when run function with new arguments.

    structure for cache:
        cache_data =
        {   "function's name1":
                {   (tuple1 of arguments): result1,
                    (tuple2 of arguments): result2,
                    ...
                    (tupleN of arguments): resultN,
                }
            "function's name2": {...}
            "function's nameN": {...}
        }
    """
    cache_data = {}

    def wrapper(*func_args, **kwargs) -> Any:
        mutable_tuple = (list, dict, set)
        if any([isinstance(arg, mutable_tuple) for arg in func_args]):
            print("Calculating new result")
            return func(*func_args, **kwargs)

        function_name = str(func)
        if function_name in cache_data:
            if func_args in cache_data[function_name]:
                print("Getting from cache")
                return cache_data[function_name][func_args]
        else:
            cache_data[function_name] = {}

        cache_data[function_name][func_args] = func(*func_args, **kwargs)
        print("Calculating new result")
        return cache_data[function_name][func_args]

    return wrapper
