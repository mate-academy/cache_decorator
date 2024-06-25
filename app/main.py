from typing import Callable, Any


def cache(func: Callable) -> Callable:
    """
    decorating only functions that take immutable arguments.
    cache should print "Getting from cache" when returns stored value
    and "Calculating new result" when run function with new arguments.

    structure for DB_cache:
        db_cache =
        {   "function's name1":
                {   (tuple1 of arguments): result1,
                    (tuple2 of arguments): result2,
                    ...
                    (tupleN of arguments): resultN,
                }
            "function's name2": {...}
            "function's nameN": {...}
        }
    """
    # 0. initialise DB_cache
    db_cache = {}

    def wrapper(*func_args, **kwargs) -> Any:
        # 1. check for immutable arguments, if not return func without caching
        mutable_tuple = (list, dict, set)
        if any([isinstance(arg, mutable_tuple) for arg in func_args]):
            print("Calculating new result")
            return func(*func_args, **kwargs)

        # 2. there are only immutable arguments - work with DB_cache

        # 3. find in DB_cache function's name and tuple of arguments
        # 3.1. find if function's name is in DB_cache
        if str(func) in db_cache:
            # 3.2 if tuple of arguments exist in DB_cache -
            # return result from cache
            if func_args in db_cache[str(func)]:
                print("Getting from cache")
                return db_cache[str(func)][func_args]

        # 4. tuple of argument doesn't exist in DB_cache
        # 4.1. check if function's name exist in DB_cache, if not - create it
        if str(func) not in db_cache:
            db_cache[str(func)] = {}

        # 4.2. if tuple of argument doesn't exist in DB_cache -
        # do new calculate and save the result to DB_cache
        db_cache[str(func)][func_args] = func(*func_args, **kwargs)
        print("Calculating new result")

        return db_cache[str(func)][func_args]

    return wrapper
