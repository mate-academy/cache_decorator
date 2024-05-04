from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def inner(*args) -> Any:
        is_already_saved = True
        working_dict = cached_data

        for value in args:
            if value not in working_dict:
                is_already_saved = False
                working_dict[value] = {}
            working_dict = working_dict[value]

        if not is_already_saved:
            print("Calculating new result")
            working_dict["result"] = func(*args)
        else:
            print("Getting from cache")

        return working_dict["result"]

    return inner
