import time

def clock_(fun):
    def inner(*args, **kwargs):
        start = time.time()
        x = fun(args, kwargs)
        print(time.time()- start)
        return x
    return inner