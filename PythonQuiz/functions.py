def f(*args):
    sum = 0
    for i in args:
       sum += (i if isinstance(i, int) else f(*i))
    return sum