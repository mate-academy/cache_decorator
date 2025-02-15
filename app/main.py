def cache(func):
    cache_data = {}

    def wrapper(*args, **kwargs):
        key = (func.__name__, args, tuple(kwargs.items()))

        if key not in cache_data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[key] = result
            return result

        print("Getting from cache")
        return cache_data[key]

    return wrapper
