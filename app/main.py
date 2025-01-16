from functools import wraps


def cache(func: tuple) -> dict:
    cache_store = {}

    @wraps(func)
    def wrapper(*args) -> dict:
        if func not in cache_store:
            cache_store[func] = {}

        if args in cache_store[func]:
            print("Getting from cache")
            return cache_store[func][args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[func][args] = result
            return result

    return wrapper


@cache
def long_time_func(num1: int, num2: int, num3: int) -> int:
    return (num1 ** num2 ** num3) % (num1 * num3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]


print(long_time_func(1, 2, 3))
print(long_time_func(1, 2, 3))
print(long_time_func_2((5, 6, 7), 2))
print(long_time_func(1, 2, 3))
print(long_time_func_2((5, 6, 7), 2))
print(long_time_func_2((5, 6, 7), 2))
