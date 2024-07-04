from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    """
    decorating only functions that take immutable arguments.
    cache should print "Getting from cache" when returns stored value
    and "Calculating new result" when run function with new arguments.

    structure for cache:
        cache_data =
        {
            ("func name1", (tuple of func_args1), frozenset(kwargs)): result1,
            ("func name1", (tuple of func_argsK), frozenset(kwargs)): resultX,
            ...
            ("func name2", (tuple of func_argsL), frozenset(kwargs)): resultY,
            ...
            ("func nameN", (tuple of func_argsM), frozenset(kwargs)): resultZ,
        }
        key = (function_name, func_args, frozenset(kwargs))
    """
    cache_data = {}

    @functools.wraps(func)
    def wrapper(*func_args, **kwargs) -> Any:
        function_name = func.__name__
        frozen_kwargs = frozenset(kwargs)

        if (function_name, func_args, frozen_kwargs) in cache_data:
            print("Getting from cache")
            return cache_data[function_name, func_args, frozen_kwargs]

        print("Calculating new result")
        func_result = func(*func_args, **kwargs)
        is_mutable_args = any(
            [isinstance(arg, (list, dict, set)) for arg in func_args])
        if not is_mutable_args:
            cache_data[function_name, func_args, frozen_kwargs] = func_result

        return func_result

    return wrapper
