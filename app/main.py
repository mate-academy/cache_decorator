from typing import Callable, Any


def cache(func: Callable) -> Callable:
    arguments_dictionary = {}

    def inner(*args, **kwargs) -> Any:
        arguments = (args, frozenset(kwargs.items()))
        if arguments not in arguments_dictionary:
            arguments_dictionary[arguments] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return arguments_dictionary[arguments]

    return inner
