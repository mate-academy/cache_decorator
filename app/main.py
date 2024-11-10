from typing import Callable, Dict, Tuple


def cache(func: Callable) -> Callable:
    cache_storage: Dict[Tuple, any] = {}

    def wrapper(*args) -> any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            return result
    return wrapper

# Example usage:


@cache
def long_running_function(first_number: int, second_number: int) -> int:
    # Simulating a long-running computation
    return first_number + second_number


@cache
def another_function(single_number: int) -> int:
    # Simulating a different long-running computation
    return single_number * 2


# Testing
print(long_running_function(1, 2))
print(long_running_function(1, 2))
print(long_running_function(2, 3))
print(another_function(3))
print(another_function(3))
