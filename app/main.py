from typing import Callable, Any


def cache(func: Callable) -> Callable:
    res_dict = {}

    def wrapper(*args) -> Any:
        if args in res_dict:
            print("Getting from cache")
            return res_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            res_dict[args] = result
            return result

    return wrapper


@cache
def long_time_func(a_a: int, b_b: int, c_c: int) -> int:
    return (a_a ** b_b ** c_c) % (a_a * c_c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result
# Calculating new result
# Calculating new result
# Getting from cache
# Calculating new result
# Getting from cache
