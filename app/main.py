from typing import Callable


def cache(func: Callable) -> Callable:
    # cache stores in dict [(data-1): result-1,  ... (data-n): result-n]
    results = {}

    def wrapper(*args, **kwargs) -> int:
        # parse kwargs dict into non-hashable format
        kwargs_tuple = tuple((key, value) for key, value in kwargs.items())
        # check is the input data is present in cache
        if (args, kwargs_tuple) in results.keys():
            print("Getting from cache")
            # return result from cache
            return results[(args, kwargs_tuple)]
        # calculate data and adding it to cache if data is not present in cache
        res = func(*args, **kwargs)
        results[(args, kwargs_tuple)] = res
        print("Calculating new result")
        return res
    return wrapper
