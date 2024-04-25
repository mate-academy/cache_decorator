from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:

        args_tuple = args + tuple(kwargs.items())
        args_hash = hash(args_tuple)

        if args_hash in cache_dict:
            print("Getting from cache")
            return cache_dict[args_hash]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[args_hash] = result
            return result

    return wrapper


@cache
def long_time_func(first: int, second: int, third: int) -> int:
    return (first ** second ** third) % (first * third)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
