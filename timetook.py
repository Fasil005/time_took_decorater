from timeit import default_timer
from functools import wraps

#decorater to print time for execution of a function
def time_took(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        res = func(*args, **kwargs)
        end_time = default_timer()
        print(f"{func.__name__.upper()} method took {end_time - start_time} seconds")
        return res
    return wrapper
