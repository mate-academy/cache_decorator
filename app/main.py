from typing import Callable


def cache(func: Callable) -> Callable:
    cache_args = {}
    resalt_func = {}
    i = [0]

    def wrapper(*args) -> any:

        if args not in cache_args:
            cache_args[i[0]] = args
            resalt = func(*args)
            resalt_func[i[0]] = resalt
            print("Calculating new result")
            i[0] += 1
            return resalt

        else:
            print("Getting from cache")
            for key, value in cache_args.items():
                if value == args:
                    args_key = key
            return resalt_func[args_key]

    return wrapper
