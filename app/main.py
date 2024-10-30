from typing import Callable

def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args):
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[args] = result
            return result

    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

long_time_func(1, 2, 3)
long_time_func(1, 2, 3)