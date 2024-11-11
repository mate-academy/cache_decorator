from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        flag = True
        while flag:
            data_iterable = tuple(
                [item for item in args if isinstance(item, (int, str, float))]
            )
            if data_iterable not in cache_dict:
                print("Calculating new result")
                cache_dict[data_iterable] = func(*args, **kwargs)
                return cache_dict[data_iterable]
            else:
                print("Getting from cache")
                return cache_dict[data_iterable]

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:  # NOQA VNE001
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
