from typing import Callable, Any

cash_dict = {}


def cache(func: Callable) -> Callable:
    def inner(*args) -> Any:
        if id(func) not in cash_dict:
            cash_dict[id(func)] = {}
        if args not in cash_dict[id(func)]:
            cash_dict[id(func)][args] = func(*args)
            print("Calculating new result")
            return cash_dict[id(func)][args]
        else:
            print("Getting from cache")
            return cash_dict[id(func)][args]
    return inner
