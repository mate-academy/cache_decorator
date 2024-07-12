from typing import Callable, Any


def cache(func: Callable, **results) -> Callable:
    #  "results" is a dictionary of completed functions(key) with result(value)
    #  in dict "cache_results" stores elements in the following form:
    #  "func(args)": result

    cache_results = {key: value for key, value in results.items()}

    def wrapper(*args) -> Any:
        data_of_func = f"{func.__name__}{args}"
        if cache_results.get(data_of_func) is None:
            result = func(*args)
            cache_results[data_of_func] = result
            print("Calculating new result")
        else:
            result = cache_results[data_of_func]
            print("Getting from cache")
        return result

    return wrapper
