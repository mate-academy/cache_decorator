from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # Creating new dictionary for saving result data
    result_dict = {}

    # Create decorator function 'wrapper', which will be responsible for
    # checking the presence the result is in the cache and saving the
    # new result.
    def wrapper(*args, **kwargs) -> Any:
        # Generating a cache key:
        # We create a key, which is a tuple of positional arguments args and a
        # tuple of named arguments tuple(kwargs.items()). Using a tuple
        # for the key allows us to work with immutable data types,
        # which is good for caching.
        key = (args, tuple(sorted(kwargs.items())))
        # If the key is already in the result_dict dictionary, we return the
        # corresponding result and print "Getting from cache".
        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]
        # If there is no key, we call the function, save the result and
        # print "Calculating new result"
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            result_dict[key] = result
            return result

    return wrapper
