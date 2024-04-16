from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = []

    def inner(*args: Any) -> Any:
        for item in storage:
            if item["arguments"] == args:
                print("Getting from cache")
                return item["result"]

        print("Calculating new result")
        result = func(*args)
        storage.append({
            "arguments": args,
            "result": result
        })
        return result

    return inner
