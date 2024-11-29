from typing import Callable, Any, Dict, Tuple


def cache(func: Callable[..., Any]) -> Callable[..., Any]:

    func._cache_storage: Dict[Tuple[Any, ...], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in func._cache_storage:
            print("Getting from cache")
            return func._cache_storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        func._cache_storage[key] = result
        return result

    return wrapper


@cache
def long_time_func(first_num: int, second_num: int, third_num: int) -> int:

    return (first_num ** second_num ** third_num) % (first_num * third_num)


@cache
def long_time_func_2(first_str: str, second_str: str) -> str:

    return f"{first_str} {second_str}"


@cache
def long_time_func_3(numbers: tuple, description: str) -> str:

    return f"{description}: {", ".join(map(str, numbers))}"


# Testing the functions
long_time_func(1, 2, 3)  # Calculating new result
long_time_func(1, 2, 3)  # Getting from cache
long_time_func(2, 2, 3)  # Calculating new result
long_time_func_3((10, 20, 30), "numbers")  # Calculating new result
long_time_func_3((10, 20, 30), "numbers")  # Getting from cache
