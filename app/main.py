from typing import Callable, Any


def cache(func: Callable) -> Callable:
    repeat_arguments = {}

    def function_result(*args: tuple[Any]) -> Any:
        result = func(*args)
        if result not in repeat_arguments:
            repeat_arguments[result] = result
            print("Getting from cache")
            return result
        print("Calculating new result")
        return result
    return function_result


@cache
def add(a: int, b: int) -> int:
    return a * 70 + b * 20


@cache
def sum_tuple(some_tuple: tuple) -> int:
    return sum(some_tuple) * 93


print(sum_tuple((5, 12, 34, 99, 15)))
print(sum_tuple((5, 12, 34, 99, 15)))
print(add(36, 48))
print(add(36, 48))
