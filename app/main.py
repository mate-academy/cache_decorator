from typing import Callable, Any


def cache(numero: int) -> Any:
    def wrapper(*args, **kwargs) -> Any:
        def inner(func: Callable) -> Any:
            results = []
            for _ in range(numero):
                results.append(func(*args, **kwargs))
                for result in results:
                    if results.count(result) > 1:
                        print(f"Getting from cache {result}")
                    else:
                        print(f"Calculating new result {result}")
        return inner
    return wrapper
