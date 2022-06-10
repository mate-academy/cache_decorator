def cache(func):
    cache_dict = {}

    def inner(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_dict[args]
    return inner
