from typing import Callable, Any
from functools import wraps

function_caches = {}


def cache(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if func not in function_caches:
            function_caches[func] = {}  # Ініціалізація кешу тільки при першому виклику

        key = (
            args,
            tuple(sorted(kwargs.items()))
        )

        if key in function_caches[func]:
            print("Getting from cache")
            return function_caches[func][key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        function_caches[func][key] = result
        return result

    return wrapper
