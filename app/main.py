from typing import Callable


def cache(func: Callable) -> Callable:
    # cache stores in format [[data-1, result-1] ... [data-n, result-n]]
    results = []

    def wrapper(*args, **kwargs) -> int:
        # check is the input data is present in cache
        if args in [_[0] for _ in results]:
            print("Getting from cache")
            # return result from cache
            return [_[1] for _ in results if _[0] == args][0]
        # calculate data and append it to cache if data is not present in cache
        res = func(*args, **kwargs)
        results.append([args, res])
        print("Calculating new result")
        return res
    return wrapper
