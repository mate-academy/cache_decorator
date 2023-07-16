import functools, typing


def cachefunc(func: Callable) -> Callable:
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[args] = result = func(*args)
        return cached_results
    return wrapper
    
