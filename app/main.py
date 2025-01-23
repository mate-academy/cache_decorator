from typing import TypeVar, Callable, Any

ImmutableType = TypeVar("ImmutableType", int, float, bool, str, tuple)


def cache(func: Callable[[tuple[Any, ...], dict[str, Any]],
          ImmutableType]) -> Callable:
    operations_cache = {}

    def wrapper(*args, **kwargs) -> ImmutableType:
        key = str(args)
        if key in operations_cache:
            print("Getting from cache")
            return operations_cache[key]

        res = func(*args, **kwargs)
        operations_cache[key] = res
        print("Calculating new result")
        return res
    return wrapper
