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
        function_name = str(func)

        if function_name in cache_data:
            if func_args in cache_data[function_name]:
                print("Getting from cache")
                return cache_data[function_name][func_args]
        else:
            cache_data[function_name] = {}

        func_result = func(*func_args, **kwargs)
        is_mutable_args = any(
            [isinstance(arg, (list, dict, set)) for arg in func_args])
        if not is_mutable_args:
            cache_data[function_name][func_args] = func_result

        print("Calculating new result")
        return func_result

    return wrapper
