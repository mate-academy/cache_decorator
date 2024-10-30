from typing import Callable, Any

def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any) -> Any:
        # Convert args to a tuple to ensure immutability
        key = tuple(args)
        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[key] = result
            return result

    return wrapper


@cache
def long_time_func(base: int, exponent: int, mod: int) -> int:
    return (base ** exponent) % mod


@cache
def long_time_func_2(numbers: tuple, power: int) -> list:
    return [number ** power for number in numbers]

