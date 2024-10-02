def cache(func: callable) -> callable:
    storage = {}

    def wrapper(*args, **kwargs) -> any:
        if args in storage:
            print("Getting from cache")
            result = storage[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[args] = result
        return result
    return wrapper
