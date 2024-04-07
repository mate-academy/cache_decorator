from typing import Callable, Any


def cache(func: Callable) -> Callable:
    completed_runs = []

    def wrapper(*args, **kwargs) -> Any:
        if completed_runs:
            for run in completed_runs:
                if run["arguments"] == (args, kwargs):
                    print("Getting from cache")
                    return run["result"]
        new_run = {
            "arguments": (args, kwargs),
            "result": func(*args, **kwargs)
        }
        completed_runs.append(new_run)
        print("Calculating new result")
        return new_run["result"]

    return wrapper
