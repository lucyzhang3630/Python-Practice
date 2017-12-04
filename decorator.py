import functools

def log(text1,text2):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text1, func.__name__))
            retval = func(*args,**kw)
            print('%s %s():' % (text2, func.__name__))
            return retval
        return wrapper
    return decorator
@log('execute before','execute after')
def now():
    print('2015-3-25')

now()
