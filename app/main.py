from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args) -> Any:
        already_saved = True
        working_dict = cache_data

        for arg in args:
            if arg not in working_dict:
                already_saved = False
                working_dict[arg] = {}
            working_dict = working_dict[arg]

        if not already_saved:
            print("Calculating new result")
            working_dict["result"] = func(*args)
        else:
            print("Getting from cache")

        return working_dict["result"]

    return inner
