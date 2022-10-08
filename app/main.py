def cache(func):
    results = {}

    def inner(*args):
        if args in results:
            print("Getting from cache")
        else:
            results[args] = func(*args)
            print("Calculating new result")
        return results[args]

    return inner
