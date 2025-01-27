from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> Any:
        cat_args = "".join([str(arg) for arg in args])
        cached_data = cache_dict.get(cat_args)
        if cached_data is None:
            print("Calculating new result")
            result_func = func(*args)
            cache_dict[cat_args] = result_func
            return result_func
        else:
            print("Getting from cache")
            return cached_data

    return wrapper


# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)


# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> int:
#     return [number ** power for number in n_tuple]


# long_time_func(1, 2, 3)
# long_time_func(2, 2, 3)
# long_time_func_2((5, 6, 7), 5)
# long_time_func(1, 2, 3)
# long_time_func_2((5, 6, 7), 10)
# long_time_func_2((5, 6, 7), 10)
