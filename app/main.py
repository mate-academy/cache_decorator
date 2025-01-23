from typing import Callable, Any

def cache(func: Callable[[str, tuple, int, float, bool], Callable]):
    operations_cache = []
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res not in operations_cache:
            operations_cache.append(res)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return operations_cache[operations_cache.index(res)]
    return wrapper
