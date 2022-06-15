def cache(func):
    dicts = {}

    def wrapper(*args):
        if args in dicts:
            print("Getting from cache")
        else:
            dicts[args] = func(*args)
            print("Calculating new result")
        return dicts[args]
    return wrapper


@cache
def long_time_func(a, b, c):
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]
