from typing import Callable
# import time


def cache(func: Callable) -> Callable:

    our_dict = {}

    def wrapper(*args) -> int:

        result = func(*args)
        if args not in our_dict:
            print("Calculating new result")
            our_dict[args] = result
        else:
            print("Getting from cache")
            return our_dict[args]

        return result

    return wrapper


# @cache
# def delay_addition(a, b):
#     time.sleep(3)
#     return a + b
#
# time1 = time.time()
# delay_addition(1, 2)
# time2 = time.time()
# delay_addition(1, 2)
# time3 = time.time()
# print(time1)
# print(time2)
# print(time3)
