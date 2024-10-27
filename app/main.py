from typing import Callable


def cache(*func: Callable) -> Callable:
    result = {}
    for fun in func:
        def decorate(*args) -> None:
            if len(result) == 0 or args not in result:
                print("Calculating new result")
                new_value = fun(*args)
                result[args] = new_value
                return new_value
            else:
                print("Getting from cache")
                return result[args]
            return result
        return decorate
