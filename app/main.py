from typing import Callable


def cache(func: Callable) -> Callable:
    cache_arguments: list = []
    cache_results: list = []

    def internal(*args, **kwargs) -> Callable:
        argument_list: list = [args, kwargs]
        for entry_index in range(len(cache_arguments)):
            if argument_list == cache_arguments[entry_index]:
                print("Getting from cache")
                return cache_results[entry_index]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_arguments.append(argument_list)
        cache_results.append(result)
        return result
    return internal
