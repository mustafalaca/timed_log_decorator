from log_and_timed_control import *
from operator import mul
from functools import reduce


@logged
@timed
def fact(n):
    return reduce(mul, range(1, n+1))


fact(5)
