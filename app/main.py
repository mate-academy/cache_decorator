def cache(func):

    caches = {}

    def wrapper(*args):
        if args not in caches.keys():
            caches[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return caches[args]

    return wrapper
