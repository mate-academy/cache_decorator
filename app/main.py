from typing import Callable

cache_storage = {}

def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        if func not in cache_storage:
            cache_storage[func] = {}
        
        cache_key = (args, frozenset(kwargs.items())) 
        if cache_key in cache_storage[func]:
            print("Getting from cache")
            return cache_storage[func][cache_key]
        
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[func][cache_key] = result
        return result
    
    return wrapper


