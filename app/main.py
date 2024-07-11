from typing import Callable, Any


def cache(func: Callable, *results) -> Callable:
    #  'results' is list of completed functions
    #  in 'cache_results' stores elements in the following order:
    #  [function name, variables], result
    cache_results = [item for item in results]

    def wrapper(*args) -> Any:
        data_of_func = [func.__name__, *args]
        if data_of_func in cache_results:
            index = cache_results.index(data_of_func)
            result = cache_results[index + 1]
            print("Getting from cache")
        else:
            result = func(*args)
            cache_results.append(data_of_func)
            cache_results.append(result)
            print("Calculating new result")
        return result
    return wrapper
