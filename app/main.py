from typing import Callable, Any, Tuple, Union
import functools

cash_dict = {}


def cache(func: Callable) -> Callable:
    @functools.wraps(func)
    def inner(*args: Tuple[Union[int, str, Tuple[int]]]) -> Any:
        if func not in cash_dict:
            cash_dict[func] = {}
        if args not in cash_dict[func]:
            cash_dict[func][args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cash_dict[func][args]
    return inner
