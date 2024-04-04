from functools import wraps


def cache(func: callable) -> callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper


@cache
def long_time_func(first_num: int, second_num: int, third_num: int) -> int:
    return (first_num ** second_num ** third_num) % (first_num * third_num)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
