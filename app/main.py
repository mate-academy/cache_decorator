def cache(func):
    dictionary = {}

    def inner(*args):
        if args in dictionary:
            print("Getting from cache")
            return dictionary[args]
        else:
            dictionary[args] = func(*args)
            print("Calculating new result")
            return dictionary[args]

        return dictionary
    return inner
