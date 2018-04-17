import functools


def catch_exception(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except AttributeError as err:
            print('{}: {}'.format(err, f.__name__))
    return func

