from typing import Callable, Dict, Any, Tuple


def cache(func: Callable) -> Callable:
    cash_storage: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args) -> Any:
        if args in cash_storage:
            print("Getting from cache")
            return cash_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cash_storage[args] = result
            return result
    return wrapper
