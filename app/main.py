from typing import Callable
stored = {}

def cache(func: Callable) -> Callable:
    def wrapper(*args):
        if (func, *args) in stored:
            print("Getting from cache")
        else:
            print("Calculating new result") 
            stored[(func, *args)] = func(*args)
        return stored[(func, *args)]
    return wrapper