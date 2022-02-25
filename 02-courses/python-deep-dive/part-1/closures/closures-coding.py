def outer_func():
    count = 0

    def incrementer():
        nonlocal count  # this is a free variable
        count = count + 1
        return count
    return incrementer


def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}-{v}' for k, v in kwargs.items()]


fn = outer_func()
# this will print 1
print(fn())
# this will print 2
print(fn())
# --------------------------------------------------------


def pow_func(n):
    def inner_func(num):
        return num**n
    return inner_func


square = pow_func(n=2)
print(square(num=9))

# ----------------------------------------------------------
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

fn1 = adders[0]
print(fn1(1))
# Here we would expect fn1 to return 2 (1 + 1). The reason that it returns 4 ist that n is
# referencing the global variable n, and the last updated value of n is 3.


def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x, y=n: x + y)
    return adders


adders = create_adders()
fn1 = adders[0]
print(fn1(1))
