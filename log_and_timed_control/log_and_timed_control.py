def logged(fn):
    from functools import wraps
    from datetime import datetime

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now()
        result = fn(*args, **kwargs)
        print('{0}: called <{1}> function'.format(run_dt, fn.__name__))
        return result

    return inner


def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print('Run time for <{0}> function: {1:.6f}s'.format(fn.__name__, elapsed))
        return result

    return inner
