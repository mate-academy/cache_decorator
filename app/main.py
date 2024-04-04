from typing import Callable


def cache(func: Callable) -> Callable:
    # cache stores in dict [(data-1): result-1,  ... (data-n): result-n]
    results = {}

    def wrapper(*args, **kwargs) -> int:
        # check is the input data is present in cache
        if args in results.keys():
            print("Getting from cache")
            # return result from cache
            return results[args]
        # calculate data and adding it to cache if data is not present in cache
        res = func(*args, **kwargs)
        results[args] = res
        print("Calculating new result")
        return res
    return wrapper
