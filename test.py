from fn.underscore import _Callable
import inspect
from functools import wraps

def sum2(arr):
    # return a function when array is callback
    if isinstance(arr, _Callable):
        return _Callable(callback=lambda x: sum(arr(x)),
                         format="sum(%s)" % arr._format,
                         arity=1
                         )
    else:
        return sum(arr)


def defer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # find _Callable positional and keyword args
        cb_args   = [ii for ii, arg in enumerate(args) if isinstance(arg, _Callable)]
        cb_kwargs = [k for k,v in kwargs.iteritems() if isinstance(v, _Callable)]
        if len(cb_args + cb_kwargs):
            # return a decorator that will call _Callable args before f
            #print cb_args, cb_kwargs
            args = list(args)
            def deferred_f(x):
                for ii in cb_args: args[ii] = args[ii](x)
                for k  in cb_kwargs: kwargs[k] = kwargs[k](x)
                return f(*args, **kwargs)
            return deferred_f
        # if no _Callables, call f
        return f(*args, **kwargs) 
    return wrapper

@defer
def sum3(a, b): return a + b
